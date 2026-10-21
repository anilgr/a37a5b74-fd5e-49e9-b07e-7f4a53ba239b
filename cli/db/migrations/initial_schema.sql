-- Schema for Kannada Word Puzzles Database

DROP TABLE IF EXISTS game_configs;
DROP TABLE IF EXISTS padagoodu_challenges;
DROP TABLE IF EXISTS padaku_challenges;
DROP TABLE IF EXISTS dictionary_words;

-- Master list of all valid words
CREATE TABLE IF NOT EXISTS dictionary_words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT UNIQUE NOT NULL,
    is_common BOOLEAN DEFAULT 0,
    length INTEGER NOT NULL
);

-- Daily challenges for Padaku (Wordle-style)
CREATE TABLE IF NOT EXISTS padaku_challenges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_date DATE UNIQUE NOT NULL,
    word_id INTEGER NOT NULL,
    FOREIGN KEY (word_id) REFERENCES dictionary_words(id)
);

-- Daily challenges for Padagoodu (Spelling Bee-style)
-- Migrated from older database
CREATE TABLE IF NOT EXISTS padagoodu_challenges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    iteration INTEGER NOT NULL,
    center_letter TEXT NOT NULL,
    letters TEXT NOT NULL,
    count INTEGER NOT NULL,
    game_date DATE UNIQUE
);

-- Global game configurations
CREATE TABLE IF NOT EXISTS game_configs (
    game_id TEXT PRIMARY KEY,
    start_date DATE NOT NULL
);
