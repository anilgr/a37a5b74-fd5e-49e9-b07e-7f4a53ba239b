const { Command } = require('commander');

module.exports = new Command("padaku")
  .description("Padaku game tools")
  .addCommand(require("./commands/find-in-api"))
  .addCommand(require("./commands/generate-api"))
  .addCommand(require("./commands/list-api-words"))
  .addCommand(require("./commands/select"))
