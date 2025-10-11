const fs = require("fs");
const path = require("path");
const { parrayOf, PArray } = require("../../utils/parray");
const { knTokenize } = require("../../utils/util");
const prompt = require("inquirer").createPromptModule();
const { Command } = require("commander");

module.exports = new Command('select')
    .argument('<file>', 'remaining words text file')
    .description('Select words from selected-words.txt')
    .option("-wl, --wordLength <wordLength>", "List word of specific word length.", 3)
    .action((file, options) => {
      file = "remaining.txt"
      const exists = fs.existsSync(file)
      const isTextFile = path.extname(file) == ".txt"

      if (exists && isTextFile) {
        const data = fs.readFileSync(file, "utf-8")
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
          parrayOf(not_selected).serialize("remaining.txt")
          let selectionFile = "selected.txt"
          const currentWOrds = fs.existsSync(selectionFile) ? PArray.deserialize(selectionFile) : []
          selected = PArray.from([...currentWOrds, ...selected])
          parrayOf(selected).serialize("selected.txt")

        })
      } else {
        if (!exists) console.log(`The file: ${path.resolve(file)} does not exist !`)
        if (!isTextFile) console.log(`Only a text file should be provided as input !`)
      }
    });
