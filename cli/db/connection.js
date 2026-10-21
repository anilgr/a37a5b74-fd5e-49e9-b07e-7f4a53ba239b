const sqlite3 = require('sqlite3').verbose();
const genericPool = require('generic-pool');
const { PADAGOODU_DB_PATH } = require('../../config/default');

/**
 * Opens a single SQLite database connection.
 * @param {string} dbPath - Path to the database file.
 * @param {number} mode - SQLite open mode (default: OPEN_READWRITE).
 * @returns {Promise<sqlite3.Database>}
 */
function openDatabase(dbPath = PADAGOODU_DB_PATH, mode = sqlite3.OPEN_READWRITE) {
    return new Promise((resolve, reject) => {
        const db = new sqlite3.Database(dbPath, mode, (err) => {
            if (err) {
                console.error("❌ Error opening database:", err.message);
                return reject(err);
            }
            console.log("✅ Database opened successfully.");
            resolve(db);
        });
    });
}

/**
 * Closes a SQLite database connection.
 * @param {sqlite3.Database} db
 * @returns {Promise<void>}
 */
function closeDatabase(db) {
    return new Promise((resolve, reject) => {
        db.close((err) => {
            if (err) {
                console.error("❌ Error closing database:", err.message);
                return reject(err);
            }
            console.log("✅ Database connection closed.");
            resolve();
        });
    });
}

/**
 * Creates a generic-pool of SQLite database connections.
 * @param {string} dbPath - Path to the database file.
 * @param {object} poolOptions - Pool configuration (max, min connections).
 * @returns {genericPool.Pool}
 */
function createConnectionPool(dbPath = PADAGOODU_DB_PATH, poolOptions = { max: 1, min: 1 }) {
    return genericPool.createPool(
        {
            create: () =>
                new Promise((resolve, reject) => {
                    const db = new sqlite3.Database(dbPath, (err) => {
                        if (err) {
                            console.error("❌ Error connecting to database:", err.message);
                            return reject(err);
                        }
                        db.configure("busyTimeout", 10000);
                        db.run("PRAGMA journal_mode = WAL", (err) => {
                            if (err) {
                                console.error("❌ Error enabling WAL mode:", err.message);
                                return reject(err);
                            }
                            console.log("✅ WAL mode enabled.");
                            resolve(db);
                        });
                    });
                }),
            destroy: (db) => closeDatabase(db),
        },
        poolOptions
    );
}

module.exports = {
    openDatabase,
    closeDatabase,
    createConnectionPool,
};
