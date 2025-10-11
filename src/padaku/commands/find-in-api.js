const { API } = require("../../utils/api");
const { Command } = require('commander');

module.exports = new Command('find')
    .argument('<word>', 'word to find')
    .description('Search for a word in api !')
    .action((word) => {
        let found = false;
        let route = undefined
        API.forEachRoute((_route) => {
            if (_route && _route.response.solution == word) {
                found = true
                route = _route
            }
        })
        if (found) {
            console.log(`Found ! \n Word: ${word}\n Path: ${route.path}`)
        } else {
            console.log(`Word ${word} is not found in API.`)
        }
    });
