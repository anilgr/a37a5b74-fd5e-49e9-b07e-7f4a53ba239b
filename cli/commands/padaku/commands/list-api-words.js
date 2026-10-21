const { API } = require("../../../core/api-service");
const { Command } = require('commander');
const { ALL_WORDS_IN_API_PATH } = require('../../../../config/default');

module.exports = new Command('list') 
    .description('List all the words in the API to all-words-in-api.txt !')
    .action(() => {
        API.getWords().serialize(ALL_WORDS_IN_API_PATH)
    });
