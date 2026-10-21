const { Route } = require("../../../core/route");
const path = require('path');
const { API } = require("../../../core/api-service");
const { PArray, parrayOf } = require("../../../utils/parray");
const { PDate } = require("../../../utils/pdate");
const { Command } = require('commander');
const {
    SELECTED_WORDS_PATH,
    IN_API_PATH,
    NOT_IN_DICTIONARY_PATH,
    VALID_SELECTION_PATH,
    PADAKU_START_DATE,
} = require('../../../../config/default');

module.exports = new Command('generate-api')
    .description('Generate static api for the words in the selected-words.txt !')
    .option('--start-date <date>', 'API write start date (YYYY-MM-DD)', '2026-03-30')
    .action((options) => {
        // get words in api 
        const wordsInAPI = parrayOf();
        API.forEachRoute(route => {
            wordsInAPI.push(route.response.solution);
        })

        // randomize, sanitize, and filter selected words
        const inAPIWords = parrayOf();
        const wordsNotInDictionary = parrayOf();
        const { DICTIONARY_WORDS: dictornaryWords } = require('../../../db/dictionary_words');

        let selectedWords = PArray.deserialize(SELECTED_WORDS_PATH);

        selectedWords = selectedWords.map((s) => s.trim()).filter(w => {
            const isInApi = wordsInAPI.contains(w)
            const isNotInDictionary = !dictornaryWords.contains(w)
            if (isNotInDictionary) { wordsNotInDictionary.push(w) }
            if (isInApi) { inAPIWords.push(w) }
            return (isInApi || isNotInDictionary) ? false : true;
        })

        inAPIWords.serialize(IN_API_PATH);
        wordsNotInDictionary.serialize(NOT_IN_DICTIONARY_PATH);

        // report stats
        if (inAPIWords.length > 0)
            console.log(`Total ${inAPIWords.length} words in the selected word list are already used in API.`);
        if (wordsNotInDictionary.length > 0)
            console.log(`${wordsNotInDictionary.length} selected words are not in dictironary.`)
        console.log(`${selectedWords.length} new words will be written to API.`);

        // generate API from the selected words.
        const apiStartDate = new PDate(PADAKU_START_DATE);
        const apiWriteStartDate = new PDate(options.startDate);
        const date = new PDate(apiWriteStartDate);

        selectedWords.serialize(VALID_SELECTION_PATH);

        selectedWords.forEach(word => {
            let route = new Route(Route.pathFromDate(date), { startDate: apiStartDate.toString(), solution: word })
            route.saveToDisk();
            date.increment();
        })

        console.log("Done.")
    });
