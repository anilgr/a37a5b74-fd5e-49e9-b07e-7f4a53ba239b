const fs = require("fs");
const path = require("path");
const { parrayOf, PArray } = require("../../../utils/parray");
const { knTokenize } = require("../../../utils/util");
const prompt = require("inquirer").createPromptModule();
const { Command } = require("commander");
const {
    REMAINING_WORDS_PATH,
    SELECTED_WORDS_PATH,
} = require('../../../../config/default');

module.exports = new Command('select')
    .description('Select words from remaining words list')
    .option("-wl, --wordLength <wordLength>", "List word of specific word length.", 3)
    .action((options) => {
      const exists = fs.existsSync(REMAINING_WORDS_PATH)

      if (exists) {
        const data = fs.readFileSync(REMAINING_WORDS_PATH, "utf-8")
        const words = data.split("\n").map((_w) => _w.trim())
        console.log(words.length)
        const filteredWords = words.filter(_w=>knTokenize(_w).length == options.wordLength)
        console.log(filteredWords.length)
        prompt([
          {
            type: "checkbox",
            name: "selected",
            message: "Select words !",
            choices: filteredWords,
            loop: false,
            pageSize: 20
          }
        ]).then(({selected}) => {
          console.log(selected)
          const not_selected = words.filter(_w=>{return selected.indexOf(_w) == -1})
          parrayOf(not_selected).serialize(REMAINING_WORDS_PATH)
          const currentWords = fs.existsSync(SELECTED_WORDS_PATH) ? PArray.deserialize(SELECTED_WORDS_PATH) : []
          const merged = PArray.from([...currentWords, ...selected])
          parrayOf(merged).serialize(SELECTED_WORDS_PATH)
        })
      } else {
        console.log(`The file: ${path.resolve(REMAINING_WORDS_PATH)} does not exist !`)
      }
    });
