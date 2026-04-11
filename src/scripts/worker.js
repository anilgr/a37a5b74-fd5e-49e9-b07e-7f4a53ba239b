const { parentPort } = require("worker_threads");
const { createCombinationGenerator } = require("../core/combination-generator");
const { kannadaAlphabet } = require("../utils/util");
const { Trie, firstNormalizeWord } = require("../core/trie");
const { PArray } = require("../utils/parray");
const { createConnectionPool } = require("../db/connection");
const { PADAGOODU_DB_PATH, WORDS_DATA_PATH } = require("../../config/default");

// Deserialize word data
const words = Array.from(new Set(PArray.deserialize(WORDS_DATA_PATH).map(w => w.trim())));
const trie = new Trie();
words.forEach(word => {
    if (firstNormalizeWord(word.trim()).length > 3)
        trie.insert(word.trim())
});

// Create a connection pool using the shared DB module
const pool = createConnectionPool(PADAGOODU_DB_PATH, { max: 1, min: 1 });

parentPort.on("message", async ({ start, end }) => {
    const db = await pool.acquire();
    db.serialize(async () => {
        console.log(`🚀 Processing range ${start} to ${end}`);

        const generator = createCombinationGenerator(kannadaAlphabet, 7);
        const batchSize = 1000;
        let batch = [];
        try {
            for (let i = 1; i <= end; i++) {
                if (i <= start) {
                    const path = generator.getNextCombination();
                    if (!path) break;
                    continue;
                }
                const path = generator.getNextCombination();
                if (!path) break;

                let count = {};
                for (let j = 0; j < path.length; j++) {
                    const subComGenerator = createCombinationGenerator(path, j + 1);
                    let subPath = subComGenerator.getNextCombination();
                    while (subPath != null) {
                        trie.getWords(subPath).forEach((word) => {
                            for (let char of subPath) {
                                count[char] ? count[char].push(word) : (count[char] = [word]);
                            }
                        });
                        subPath = subComGenerator.getNextCombination();
                    }
                }

                for (let key in count) {
                    if (count[key].flat().length >= 20) {
                        batch.push([i, key, path.join(""), count[key].flat().length]);

                        if (batch.length >= batchSize) {
                            try {
                                await insertBatchWithRetry(db, batch);
                                batch = [];
                            } catch (e) {
                                console.error("❌ Batch insert failed:", e.message);
                            }
                        }
                    }
                }
            }

            if (batch.length > 0) {
                try {
                    await insertBatchWithRetry(db, batch);
                } catch (e) {
                    console.error("❌ Final batch insert failed:", e.message);
                }
            }
        } finally {
            pool.release(db);
        }

        parentPort.postMessage(`✅ Completed range ${start} to ${end}`);
    })
});

// Insert function with retry mechanism
async function insertBatchWithRetry(db, batch, retries = 5, delay = 100) {
    for (let attempt = 0; attempt < retries; attempt++) {
        try {
            await new Promise((resolve, reject) => {
                db.serialize(() => {
                    db.run("BEGIN TRANSACTION");

                    // Construct bulk insert query
                    const placeholders = batch.map(() => "(?, ?, ?, ?)").join(",");
                    const values = batch.flat(); // Flatten the batch array

                    const sql = `INSERT INTO padagoodu (iteration, center_letter, letters, count) VALUES ${placeholders}`;

                    db.run(sql, values, function (err) {
                        if (err) {
                            console.error("❌ Bulk Insert Error:", err.message);
                            db.run("ROLLBACK");
                            return reject(err);
                        }
                        db.run("COMMIT", (commitErr) => {
                            if (commitErr) {
                                console.error("❌ Commit failed:", commitErr.message);
                                return reject(commitErr);
                            }
                            console.log(`✅ Bulk Insert Successful: Last ID ${batch[batch.length - 1][0]}`);
                            resolve();
                        });
                    });
                });
            });
            return; // Success, exit function
        } catch (err) {
            console.error(`⚠️ Retrying batch... Attempt ${attempt + 1}`);
            await new Promise(res => setTimeout(res, delay * (2 ** attempt))); // Exponential backoff
        }
    }
    console.error("❌ Maximum retries reached, batch failed.");
}

// Properly clean up the pool on worker exit
process.on("exit", () => {
    pool.drain().then(() => pool.clear());
});

// Handle termination signals
process.on('SIGINT', () => {
    console.log("⚠️ Termination signal received. Saving progress...");
});
