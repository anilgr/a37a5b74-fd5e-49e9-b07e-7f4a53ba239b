const { API } = require("../api");

module.exports = (program) => {
  program
    .command('list')
    .description('List all the words in the API to all-words-in-api.txt !')
    .action(() => {
        API.getWords().serialize("all-words-in-api.txt")
    });
};
