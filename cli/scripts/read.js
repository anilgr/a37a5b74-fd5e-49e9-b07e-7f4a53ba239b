const { createCombinationGenerator } = require('../core/combination-generator');
const { PArray } = require('../utils/parray');
const path = require('path');
const { writeFileSync } = require('fs');
const { Trie } = require('../core/trie');
const { openDatabase, closeDatabase } = require('../db/connection');
const { PADAGOODU_DB_PATH, FREQ_PATH } = require('../../config/default');

// Note: 'trie' needs to be initialised before use. 
// This script references a 'trie' from a removed combination-generator export.
// If you need a trie here, initialise it as in worker.js.

function getWordsInPath(letterPath, letter, trie) {
    try {
        let count = []
        for (let i = 0; i < letterPath.length; i++) {
            const subComGenerator = createCombinationGenerator(letterPath, i + 1);
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

function diff(one, two) {
    return one.filter((w) => (two.indexOf(w) == -1))
}

// Open the database and process rows
openDatabase(PADAGOODU_DB_PATH, require('sqlite3').OPEN_READONLY).then(db => {
    const ids = PArray.deserialize(FREQ_PATH);

    db.each(`SELECT * FROM padagoodu where id in (${ids.join(",")}) order by random()`, [], (err, row) => {
        if (err) {
            console.error("❌ Error reading data:", err.message);
            return;
        }

        // TODO: initialise trie before running this script
        // const words = getWordsInPath(row.letters, row.center_letter)

        // if (words.length != 0) {
        //     writeFileSync('rows.txt', `${row.id}, ${row.iteration}, ${row.center_letter}, ${row.letters}, ${row.count}, [ ${words.join(", ")} ]\n`, { encoding: 'utf-8', flag: "a" });
        // }
    }, (err, count) => {
        if (err) {
            console.error(err.message);
        } else {
            console.log(`Total rows processed: ${count}`);
        }
        closeDatabase(db);
    });
}).catch(err => {
    console.error("❌ Failed to open database:", err.message);
});

module.exports = {
    getWordsInPath,
    diff,
};