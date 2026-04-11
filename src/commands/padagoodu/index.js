const { Command } = require('commander');

module.exports = new Command('padagoodu')
  .description('Padagoodu commands manage game data/api')
  .addCommand(require("./commands/generate-api"));
