const path = require("path")
const { parrayOf, PArray } = require("../utils/parray")
const { DATA_DIR } = require('../../config/default')

const DICTIONARY_WORDS =  parrayOf(
    ...[
        ...PArray.deserialize(path.join(DATA_DIR, 'data_3.txt')),
        ...PArray.deserialize(path.join(DATA_DIR, 'data_4.txt')),
        ...PArray.deserialize(path.join(DATA_DIR, 'data_5.txt')),
    ])

module.exports = {
    DICTIONARY_WORDS
}