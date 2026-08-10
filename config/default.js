const path = require('path');

// Project root directory
const PROJECT_ROOT = path.join(__dirname, '..');

// Base path for the API static files (year/month/day JSON structure)
const API_BASE_PATH = PROJECT_ROOT;

// Central data directory for all text files and databases
const DATA_DIR = path.join(PROJECT_ROOT, 'data');

// Database paths
const PADAGOODU_DB_PATH = path.join(DATA_DIR, 'combinations_latest_latest.db');

// Data file paths
const SELECTED_WORDS_PATH = path.join(DATA_DIR, 'selected.txt');
const REMAINING_WORDS_PATH = path.join(DATA_DIR, 'remaining.txt');
const ALL_WORDS_IN_API_PATH = path.join(DATA_DIR, 'all-words-in-api.txt');
// Padaku intermediate/temp output paths
const PADAKU_TEMP_DIR = path.join(PROJECT_ROOT, 'src', 'commands', 'padaku', 'temp');
const IN_API_PATH = path.join(PADAKU_TEMP_DIR, 'in-api.txt');
const NOT_IN_DICTIONARY_PATH = path.join(PADAKU_TEMP_DIR, 'not-in-dictionary.txt');
const VALID_SELECTION_PATH = path.join(PADAKU_TEMP_DIR, 'valid-selection.txt');
const FREQ_PATH = path.join(DATA_DIR, 'freq.txt');
const WORDS_DATA_PATH = path.join(DATA_DIR, 'words_data.txt');

// Default game start dates
const PADAKU_START_DATE = '2024-01-05';
const PADAGOODU_START_DATE = '2025-03-12';

module.exports = {
    PROJECT_ROOT,
    API_BASE_PATH,
    DATA_DIR,
    PADAGOODU_DB_PATH,
    SELECTED_WORDS_PATH,
    REMAINING_WORDS_PATH,
    ALL_WORDS_IN_API_PATH,
    IN_API_PATH,
    NOT_IN_DICTIONARY_PATH,
    PADAKU_TEMP_DIR,
    VALID_SELECTION_PATH,
    FREQ_PATH,
    WORDS_DATA_PATH,
    PADAKU_START_DATE,
    PADAGOODU_START_DATE,
};
