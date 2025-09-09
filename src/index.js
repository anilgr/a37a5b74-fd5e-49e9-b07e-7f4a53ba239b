const { Command } = require('commander');

const program = new Command("")
    .description('Word puzzle CLI')
    .version('1.0.0')

program.addCommand(require("./padaku"));
program.addCommand(require("./padagoodu"))

program.parse(process.argv);
