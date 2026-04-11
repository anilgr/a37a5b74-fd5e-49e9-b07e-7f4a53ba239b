const { PArray } = require("../utils/parray");
const { SELECTED_WORDS_PATH } = require("../../config/default");

// Randomize selected words
PArray.deserialize(SELECTED_WORDS_PATH).randomize().serialize(SELECTED_WORDS_PATH);
