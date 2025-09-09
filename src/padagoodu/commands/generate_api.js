const fs = require('fs');
const path = require('path');
const { PArray } = require("../../utils/parray");
const { API_BASE_PATH } = require('../../globals');
const { Command } = require('commander');
const sqlite3 = require('sqlite3').verbose();

const START_DATE = new Date("2025-03-12");

module.exports = new Command('generate-api')
  .description('Generate static API based on dates as path names in API_BASE_PATH')
  .action(() => {
    const dbPath = path.join(__dirname, 'combinations_latest_latest.db');
    // const db = new sqlite3.Database(dbPath);
    // // Open the database
    const db = new sqlite3.Database(dbPath, sqlite3.OPEN_READWRITE, (err) => {
      if (err) {
        console.error("❌ Error opening database:", err.message);
        return;
      }

      console.log("✅ Database opened successfully.");
      let currentDate = new Date(START_DATE);
      const updates = [];
      const ids = PArray.deserialize(path.join(__dirname, 'freq.txt'))

      db.serialize(() => {
        db.all(`SELECT id, center_letter, letters FROM padagoodu WHERE id IN (${ids.join(", ")}) ORDER BY RANDOM() LIMIT 300`, (err, rows) => {
          if (err) {
            console.error("Error selecting data:", err.message);
            db.close();
            return;
          }
          console.log(rows)
          rows.forEach(row => {
            const year = currentDate.getFullYear();
            const month = String(currentDate.getMonth() + 1).padStart(2, '0');
            const day = String(currentDate.getDate()).padStart(2, '0');
            const datePath = path.join(API_BASE_PATH, 'pagoodu', year.toString(), month);

            if (!fs.existsSync(datePath)) {
              fs.mkdirSync(datePath, { recursive: true });
            }

            const filePath = path.join(datePath, `${day}.json`);
            fs.writeFileSync(filePath, JSON.stringify({ id: row.id, centerLetter: row.center_letter, letters: row.letters, startDate: `${START_DATE.getFullYear()}/${String(START_DATE.getMonth()).padStart(2, '0')}/${String(START_DATE.getDate()).padStart(2, '0')}` }, null, 2));

            // Collect the update for the row
            updates.push({ id: row.id, game_date: currentDate.toISOString().split('T')[0] });

            // Increment the date
            currentDate.setDate(currentDate.getDate() + 1);
          });

          if (updates.length === 0) {
            console.log("No rows to update. Exiting.");
            db.close();
            return;
          }

          // Perform batch update within a transaction
          db.run("BEGIN TRANSACTION", (err) => {
            if (err) {
              console.error("Transaction start failed:", err.message);
              db.close();
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
                      db.close((err) => {
                        if (err) {
                          console.error("Error closing database:", err.message);
                        } else {
                          console.log("Database updates completed and connection closed.");
                        }
                      });
                    });
                  });
                }
              });
            });
          });
        });
      });
    })
  });

