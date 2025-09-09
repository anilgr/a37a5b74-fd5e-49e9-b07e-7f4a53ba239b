const { Command } = require('commander');

module.exports = new Command('padagoodu')
  .description('Pagoodu commands manage game data/api')
  .addCommand(require("./commands/get_words"))
  .addCommand(require("./commands/generate_api"));
