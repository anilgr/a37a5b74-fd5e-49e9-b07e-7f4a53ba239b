const { openDatabase, closeDatabase } = require('../db/connection');
const { PArray } = require('../utils/parray');
const { PADAGOODU_DB_PATH, FREQ_PATH, WORDS_DATA_PATH } = require('../../config/default');
const { Trie, firstNormalizeWord } = require('../core/trie');
const { createCombinationGenerator } = require('../core/combination-generator');
const fs = require('fs');

(async () => {
    console.log('🔄 Initializing Trie and loading word dictionary...');
    const words = Array.from(new Set(PArray.deserialize(WORDS_DATA_PATH).map(w => w.trim())));
    const trie = new Trie();
    words.forEach(word => {
        if (firstNormalizeWord(word.trim()).length > 3) {
            trie.insert(word.trim());
        }
    });

    function getWordsInPath(letterPath, letter) {
        let count = [];
        for (let i = 0; i < letterPath.length; i++) {
            const subComGenerator = createCombinationGenerator(letterPath, i + 1);
            let subPath = subComGenerator.getNextCombination();
            while (subPath != null) {
                if (subPath.indexOf(letter) != -1) {
                    count.push(...trie.getWords(subPath.join('')));
                }
                subPath = subComGenerator.getNextCombination();
            }
        }
        return count;
    }

    function diff(one, two) {
        return one.filter(w => two.indexOf(w) == -1);
    }

    const db = await openDatabase(PADAGOODU_DB_PATH);

    // 1. Load games assigned in the last 6 months (2026-01-08 to 2026-07-08)
    db.all("SELECT id, center_letter, letters FROM padagoodu WHERE game_date >= '2026-01-08' AND game_date <= '2026-07-08'", (err, recentRows) => {
        if (err) {
            console.error("❌ Error querying recent games:", err.message);
            closeDatabase(db);
            return;
        }

        console.log(`✅ Loaded ${recentRows.length} recent games from the last 6 months.`);
        const recentWordsMap = new Map();
        recentRows.forEach(r => recentWordsMap.set(r.id, getWordsInPath(r.letters, r.center_letter)));

        const existingFreqIds = PArray.deserialize(FREQ_PATH).map(Number);
        const freqIdsSet = new Set(existingFreqIds);
        console.log(`✅ Current IDs in freq.txt: ${existingFreqIds.length}`);

        // 2. Query all unassigned candidate games with word count between 20 and 25
        db.all("SELECT id, center_letter, letters, count FROM padagoodu WHERE (game_date IS NULL OR game_date = '') AND count >= 20 AND count <= 25 ORDER BY id ASC", (err2, candidateRows) => {
            if (err2) {
                console.error("❌ Error querying candidates:", err2.message);
                closeDatabase(db);
                return;
            }

            const candidates = candidateRows.filter(r => !freqIdsSet.has(Number(r.id)));
            console.log(`✅ Unassigned candidate games (20-25 words): ${candidates.length}`);

            const selected = [];
            const selectedWordsMap = new Map();

            candidates.forEach(cand => {
                const candWords = getWordsInPath(cand.letters, cand.center_letter);
                if (candWords.length === 0) return;

                let isDistinct = true;

                // Check against last 6 months
                for (let [recId, recWords] of recentWordsMap.entries()) {
                    const diffA = diff(candWords, recWords);
                    const overlap = (1 - (diffA.length / candWords.length)) * 100;
                    if (overlap > 50) {
                        isDistinct = false;
                        break;
                    }
                }

                // Check against already selected new candidates
                if (isDistinct) {
                    for (let [selId, selWords] of selectedWordsMap.entries()) {
                        const diffA = diff(candWords, selWords);
                        const overlap = (1 - (diffA.length / candWords.length)) * 100;
                        if (overlap > 50) {
                            isDistinct = false;
                            break;
                        }
                    }
                }

                if (isDistinct) {
                    selected.push(cand);
                    selectedWordsMap.set(cand.id, candWords);
                }
            });

            console.log(`🚀 Selected ${selected.length} unique puzzles (<= 50% overlap against last 6 months and each other).`);

            if (selected.length === 0) {
                console.log("⚠️ No clean puzzles found. Exiting.");
                closeDatabase(db);
                return;
            }

            // 3. Append selected IDs to freq.txt
            const appendData = selected.map(cand => cand.id).join('\n') + '\n';
            fs.appendFileSync(FREQ_PATH, appendData, { encoding: 'utf-8' });
            console.log(`✅ Appended ${selected.length} new IDs to freq.txt. Total IDs in freq.txt now: ${existingFreqIds.length + selected.length}`);

            closeDatabase(db);
        });
    });
})();
