const fs = require('fs');
const { Route } = require("../../../core/route");
const path = require('path');
const { PArray } = require("../../../utils/parray");
const { Command } = require('commander');
const { openDatabase, closeDatabase } = require('../../../db/connection');

const {
  API_BASE_PATH,
  PADAGOODU_DB_PATH,
  FREQ_PATH,
  PADAGOODU_START_DATE,
} = require('../../../../config/default');

module.exports = new Command('generate-api')
  .description('Generate static API based on dates as path names in API_BASE_PATH')
  .option('--start-date <date>', 'Game start date (YYYY-MM-DD)', PADAGOODU_START_DATE)
  .action(async (options) => {
    const START_DATE = new Date(options.startDate);

    const db = await openDatabase(PADAGOODU_DB_PATH);

    let currentDate = new Date(START_DATE);
    const updates = [];
    const ids = PArray.deserialize(FREQ_PATH);

    db.serialize(() => {
      if (!ids || ids.length === 0) {
        console.log("No ids found in freq.txt. Exiting.");
        closeDatabase(db);
        return;
      }

      // Select remaining unassigned games (game_date NULL or empty) from the set in freq.txt
      db.all(`SELECT id, center_letter, letters FROM padagoodu WHERE (game_date IS NULL OR game_date = '') AND id IN (${ids.join(", ")}) ORDER BY RANDOM()`, (err, rows) => {
        if (err) {
          console.error("Error selecting data:", err.message);
          closeDatabase(db);
          return;
        }
        console.log(rows)
        rows.forEach(row => {
          const response = { 
            id: row.id, 
            centerLetter: row.center_letter, 
            letters: row.letters, 
            startDate: `${START_DATE.getFullYear()}/${String(START_DATE.getMonth() + 1).padStart(2, '0')}/${String(START_DATE.getDate()).padStart(2, '0')}` 
          };
          const route = new Route(Route.pathFromDate(currentDate, 'pagoodu'), response);
          route.saveToDisk();
 // Collect the update for the row
          updates.push({ id: row.id, game_date: currentDate.toISOString().split('T')[0] });

          // Increment the date
          currentDate.setDate(currentDate.getDate() + 1);
        });

        if (updates.length === 0) {
          console.log("No rows to update. Exiting.");
          closeDatabase(db);
          return;
        }

        // Perform batch update within a transaction
        db.run("BEGIN TRANSACTION", (err) => {
          if (err) {
            console.error("Transaction start failed:", err.message);
            closeDatabase(db);
            return;
          }

          const stmt = db.prepare("UPDATE padagoodu SET game_date = ? WHERE id = ?");
          let pendingUpdates = updates.length;

          updates.forEach(update => {
            stmt.run(update.game_date, update.id, (err) => {
              if (err) {
                console.error("Error updating row:", err.message);
              }
              pendingUpdates--;

              if (pendingUpdates === 0) {
                stmt.finalize((err) => {
                  if (err) {
                    console.error("Error finalizing statement:", err.message);
                  }

                  db.run("COMMIT", (err) => {
                    if (err) {
                      console.error("Transaction commit failed:", err.message);
                    }
                    closeDatabase(db);
                    console.log("Database updates completed.");
                  });
                });
              }
            });
          });
        });
      });
    });
  });
