const { getWordsInApi } = require('./util.js')
require('./extension_functions.js')
const words = getWordsInApi();
words.serialize('../words-in-api.txt')