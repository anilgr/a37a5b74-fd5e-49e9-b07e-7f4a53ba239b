const { Command } = require('commander');

module.exports = new Command('padanoolu')
  .description('Padanoolu game commands and API tools')
  .addCommand(require('./commands/generate-api'));
