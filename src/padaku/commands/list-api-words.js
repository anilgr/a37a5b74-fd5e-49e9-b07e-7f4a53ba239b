const { API } = require("../../utils/api");
const { Command } = require('commander');

module.exports = new Command('list') 
    .description('List all the words in the API to all-words-in-api.txt !')
    .action(() => {
        API.getWords().serialize("all-words-in-api.txt")
    });
