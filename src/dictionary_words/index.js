const path = require("path")
const { parrayOf, PArray } = require("../utils/parray")

const DICTIONARY_WORDS =  parrayOf(
    ...[
        ...PArray.deserialize(path.join(__dirname, 'data_3.txt')),
        ...PArray.deserialize(path.join(__dirname, 'data_4.txt')),
        ...PArray.deserialize(path.join(__dirname, 'data_5.txt')),
    ])

module.exports = {
    DICTIONARY_WORDS
}