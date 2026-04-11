const { Command } = require('commander');

const program = new Command("")
    .description('Word puzzle CLI')
    .version('1.0.0')

program.addCommand(require("./commands/padaku"));
program.addCommand(require("./commands/padagoodu"))

program.parse(process.argv);
