const { API_BASE_PATH } = require("../globals");
const { API } = require("./api");
const { PArray, parrayOf } = require("./parray");
const { PDate } = require("./pdate");
const { Route } = require("./route");
const { pathFromDate } = require("./util");
const path = require('path');

// get words in api 
const wordsInAPI = parrayOf();
API.forEachRoute(route => {
    wordsInAPI.push(route.response.solution);
})

// randomize, sanitize, and filter selected words
const inAPIWords = parrayOf();
const wordsNotInDictionary = parrayOf();
const dictornaryWords = parrayOf(
    ...[
        ...PArray.deserialize('../../data_3.txt'), 
        ...PArray.deserialize('../../data_4.txt'),
        ...PArray.deserialize('../../data_5.txt')
    ])

let selectedWords = PArray.deserialize(path.join(API_BASE_PATH, 'selected-words.txt'));

selectedWords = selectedWords.map((s) => s.trim()).filter(w => {
    const isInApi = wordsInAPI.contains(w)
    const isNotInDictionary = !dictornaryWords.contains(w)
    if (isNotInDictionary) { wordsNotInDictionary.push(w) }
    if (isInApi) { inAPIWords.push(w) }
    return (isInApi || isNotInDictionary) ? false : true;
})

wordsNotInDictionary.serialize("not-in-dictionary.txt");
// selectedWords.serialize(path.join(API_BASE_PATH, 'selected-words.txt'))

// report stats
if (inAPIWords.length > 0)
    console.log(`Total ${inAPIWords.length} words in the selected word list are already used in API.`);
if (wordsNotInDictionary.length > 0)
    console.log(`${wordsNotInDictionary.length} selected words are not in dictironary: `, wordsNotInDictionary)
console.log(`${selectedWords.length} new words will be written to API.`);

// generate API from the selected words.
const apiStartDate = new PDate("2024-01-05")
const apiWriteStartDate = new PDate('2024-04-05');
const date = new PDate(apiWriteStartDate);

selectedWords.forEach(word => {
    let route = new Route(pathFromDate(date), { startDate: apiStartDate.toString(), solution: word })
    route.saveToDisk();
    date.increment();
})

console.log("Done.")