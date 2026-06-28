# Kannada Word Puzzles - Database Consolidation Summary
*Generated: 2026-04-12*

## 1. Database Overview
**File**: `data/kannada_puzzles.db`

| Entity | Total Count |
| :--- | :--- |
| **Unique Words** (Master Dictionary) | 111,277 |
| **Padaku** (Wordle) Challenges | 906 |
| **Padagoodu** (Spelling Bee) Challenges | 8,080 |
| **Game Configs** (Metadata) | 2 |

---

## 2. Word Commonality Statistics
**Current Common Words in DB (`is_common = 1`)**: 10,795
*(Sourced from `remaining.txt` + Historical Solution folders)*

### Comparison with `words_data.txt` (11,065 words)
- **Overlap**: 7,072 words are present in both.
- **Missing from DB**: 3,993 words in `words_data.txt` are NOT marked common in DB. (See `missing_common_words.txt`)
- **Extra in DB**: 3,723 words in DB are marked common but are NOT in `words_data.txt`. (See `common_in_db_not_in_words_data.txt`)

### Normalized Length Analysis (Trie.js Logic)
- **Min Normalized Length**: 2
- **Sample words (Len 2)**: ಆಯಾಯ, ಏಕಕ, ಕಣಕ, ಕಥಕ್, ಕಥಕ, ಗಗ್ಗರ, ಜಲಜ, ನಟನ
- **Full Report**: See `data/common_in_db_word_lengths.txt`

---

## 3. Padaku (Wordle) History
- **Total Challenges**: 906
- **Date Range**: 2024-01-05 to 2026-06-28
- **First Word**: ಕಡಲು (2024-01-05)
- **Last Word**: ಸಹಮತ (2026-06-28)

---

## 4. Padagoodu (Spelling Bee) Data
- **Total Challenges**: 8,080 (484 dated)
- **Date Range**: 2025-03-12 to 2026-07-08

### Word Count Extremes
- **Highest Count**: 56 words (Iteration `32608137`, Center: `ರ`)
- **Lowest Count**: 20 words (Iteration `32381905`, Center: `ಸ`)

---

## 5. Data Source Audit
*Explaining the difference between raw lines and unique database words.*

| Source File | Raw Lines | Unique Words | Deduplication Loss |
| :--- | :--- | :--- | :--- |
| `data_3/4/5.txt` | 121,065 | 111,277 | ~8% |
| `remaining.txt` | 28,326 | 9,891 | ~65% (!) |
| `words_data.txt` | 11,065 | 11,065 | 0% |
