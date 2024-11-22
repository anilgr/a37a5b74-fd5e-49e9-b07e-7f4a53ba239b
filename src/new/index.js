const { Command } = require('commander');
const fs = require('fs');
const path = require('path');

const program = new Command();
program.version('1.0.0');

const commandsPath = path.join(__dirname, 'utils');

// Dynamically load all command files
fs.readdirSync(commandsPath).forEach((file) => {
  if (file.endsWith('.js')) {
    const command = require(path.join(commandsPath, file));
    command(program);
  }
});

program.parse(process.argv);
