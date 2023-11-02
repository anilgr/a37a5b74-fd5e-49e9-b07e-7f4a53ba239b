// get words from tomorrow in the api
const fs = require('fs')
const path = require('path')
const { getWordsInApi } = require('./util.js')
require('./extension_functions.js')

const today = new Date();
const tomorrow = new Date(today);
tomorrow.setDate(today.getDate() + 1);

let year = tomorrow.getFullYear();
let month = tomorrow.getMonth() + 1;
let day = tomorrow.getDate();


// Create the directory path in the format "year/month"
const directoryPath = path.join(__dirname, `../${year}/${String(month).padStart(2, '0')}`);

// Create the JSON file inside the directory
const filePath = path.join(directoryPath, `${String(day).padStart(2, '0')}.json`);

if (fs.existsSync(filePath)) {
    const data = fs.readFileSync(filePath, { encoding: 'utf-8' })
    console.log(data)
    if (data !== null) {
        const word = JSON.parse(data).solution.trim()
        const wordsInApi = getWordsInApi();
        const wordIndex = wordsInApi.indexOf(word)
        const futureWOrdsInApi = wordsInApi.slice(wordIndex)
        const selectedWords = Array.deserialize("../selected-words.txt")
        const randomizedWords = [...futureWOrdsInApi, ...selectedWords].randomize()
        console.log({selectedWords, wordsInApi, randomizedWords})
        randomizedWords.serialize("../selected-words.txt")
    }
}




