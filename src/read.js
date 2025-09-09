const { createCombinationGenerator } = require('./combination_generator');
const { PArray } = require('./src/new/parray');
const path = require('path')
// const { kannadaAlphabet } = require('./src/new/util');

const { writeFileSync } = require('fs');
const { trie } = require('./combination-generator');

const sqlite3 = require('sqlite3').verbose();

function getWordsInPath(path, letter) {
    try {
        let count = []
        for (let i = 0; i < path.length; i++) {
            const subComGenerator = createCombinationGenerator(path, i + 1);
            let subPath = subComGenerator.getNextCombination();
            while (subPath != null) {
                if ((subPath.indexOf(letter) != -1))
                    count.push(...trie.getWords(subPath.join("")))
                subPath = subComGenerator.getNextCombination();
            }
        }
        return count
    } catch (e) {
        console.log("Error", e)
        return []
    }
}


// const wordsmap = new Map()
// const freqMap = new Map()

// Open the database
const db = new sqlite3.Database('combinations_latest_latest.db', sqlite3.OPEN_READONLY, (err) => {
    if (err) {
        console.error("❌ Error opening database:", err.message);
        return;
    }

    const ids = PArray.deserialize(path.join(__dirname, 'freq.txt'))

    console.log("✅ Database opened successfully.");
    // Query and print rows after connection is established
    db.each(`SELECT * FROM padagoodu where id in (${ids.join(",")}) order by random()`, [], (err, row) => {
        if (err) {
            console.error("❌ Error reading data:", err.message);
            return;
        }

        const words = getWordsInPath(row.letters, row.center_letter)

        // wordsmap.set(row.id, words)

        if (words.length != 0) {
            writeFileSync('rows.txt', `${row.id}, ${row.iteration}, ${row.center_letter}, ${row.letters}, ${row.count}, [ ${words.join(", ")} ]\n`, { encoding: 'utf-8', flag: "a" });
        }
        // })
    }, (err, count) => {
        if (err) {
            console.error(err.message);
        } else {
            console.log(`Total rows processed: ${count}`);
            // writeFileSync('all_words.txt', Array.from(wordset).join("\n"))
            // wordsmap.forEach((words, id) => {
            //     // let highest = 0
            //     wordsmap.forEach((otherWords, otherId) => {
            //         if (otherId != id) {
            //             const diffA = diff(words, otherWords)
            //             const freq = (1 - (diffA.length / words.length)) * 100
            //             if (freq > 50)
            //                 freqMap.set(id, (freqMap.get(id) || 0) + 1)
            //         }
            //     })

            // })

            // let ids = Array.from(wordsmap.keys());
            // while(ids.length != 0) {
            //     id = ids.shift();
            //     wordsmap.forEach((otherWords, otherId) => {
            //         if (otherId != id) {
            //             const words = wordsmap.get(id)
            //             const diffA = diff(words, otherWords)
            //             const freq = (1 - (diffA.length / words.length)) * 100
            //             if (freq > 50) {
            //                 freqMap.set(id, [...(freqMap.get(id) || []), otherId])
            //                 ids = ids.filter(_id=>_id!=otherId)
            //             }
            //         }
            //     })
            // }

            // freqMap.forEach((value, id) => {
            //     writeFileSync('freq.txt', `${id}\n`, { encoding: 'utf-8', flag: 'a' })
            // })
        }
        // Close the database after all rows are processed
        db.close((err) => {
            if (err) {
                console.error("Error closing the database:", err.message);
            } else {
                console.log("Database connection closed.");
            }
        });
    });

});

function diff(one, two) {
    return one.filter((w) => (two.indexOf(w) == -1))
}

// const processBatch = async (db, batchSize, offset) => {
//     return new Promise((resolve, reject) => {
//         db.all(`SELECT * FROM your_table LIMIT ? OFFSET ?`, [batchSize, offset], (err, rows) => {
//             if (err) {
//                 reject(err);
//             } else {
//                 rows.forEach(row => console.log(row)); // Process each row
//                 resolve(rows.length);
//             }
//         });
//     });
// };

// const processAllRows = async () => {
//     const db = new sqlite3.Database('your_database.db');
//     let offset = 0;
//     const batchSize = 1000; // Adjust batch size based on memory

//     while (true) {
//         const rowCount = await processBatch(db, batchSize, offset);
//         if (rowCount === 0) break; // Stop when no more rows
//         offset += batchSize;
//     }

//     db.close();
//     console.log("Processing complete");
// };

// processAllRows();

// const normalizeWord = (word) => {
//     return Array.from(new Set(word.split("").filter(char => !(halantExp.test(char) || diacriticToVowelMap.has(char) || anuswara_visargeExp.test(char))))).sort().join("")
// }

// const words = Array.from(new Set(PArray.deserialize("./src/dict.txt").map(w => w.trim())));
// const panagrams = new Set()
// words.forEach(word=>{
//     const normalized = normalizeWord(word);
//     if(normalized.length == 7) {
//         panagrams.add(word)
//     }
// })

// console.log([...panagrams])

// const gen = createCombinationGenerator(kannadaAlphabet, 7);
// const end = 85900584
// for(let i=0; i < end; i++) {
//     const path = gen.getNextCombination()
//     if(i < end - 1) {
//         continue
//     }
//     console.log(path)
// }
// [
//   'ಂ', 'ಃ', 'ಅ',
//   'ಆ', 'ಇ', 'ಈ',
//   'ಉ'
// ]