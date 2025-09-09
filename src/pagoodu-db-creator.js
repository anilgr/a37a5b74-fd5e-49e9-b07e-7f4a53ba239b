const { Worker } = require('worker_threads');
const sqlite3 = require('sqlite3').verbose();

// Create SQLite database connection (only in the main thread)
const db = new sqlite3.Database('combinations_latest_latest.db', (err) => {
    if (err) console.error("❌ Database connection error:", err.message);
    else {
        console.log("✅ Connected to SQLite database.");

        // Ensure table exists before workers start inserting data
        db.run(`CREATE TABLE IF NOT EXISTS padagoodu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            iteration INTEGER NOT NULL,
            center_letter TEXT NOT NULL,
            letters TEXT NOT NULL,
            count INTEGER NOT NULL,
            game_date DATE UNIQUE 
        )`, (err) => {
            if (err) {
                console.error("❌ Error creating table:", err.message);
            } else {
                console.log("✅ Table ensured. Spawning workers...");

                // Close main DB connection (workers will have their own)
                db.close();

                const NUM_WORKERS = 8; // Adjust based on your CPU cores
                const workers = [];
                // Distribute the range of iterations across workers
                const iterationsPerWorker = Math.ceil(85900584 / NUM_WORKERS);

                for (let i = 0; i < NUM_WORKERS; i++) {
                    const worker = new Worker('./worker.js');
                    const start = Math.max(i * iterationsPerWorker, 1);
                    const end = Math.min(start + iterationsPerWorker, 85900584);
                    worker.postMessage({ start, end });
                    worker.on('message', (msg) => {
                        if (msg.ready) {

                        } else if (msg.error) {
                            console.error("Main: Worker reported an error:", msg.error);
                        } else if (msg.success) {
                            console.log("Main: Worker successfully processed the batch.");
                        }
                    });

                    worker.on('error', (err) => {
                        console.error("Main: Worker error:", err);
                    });

                    workers.push(worker);
                }

            }
        });
    }
});


