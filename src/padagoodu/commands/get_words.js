const { Command } = require("commander");
const fs = require("fs");
const path = require("path");
const { API_BASE_PATH } = require('../../globals');

module.exports = new Command("some_command")
    .description("does someting")
    .action(() => {
        console.log("Doing something !");
        fs.writeFileSync(path.join(__dirname, "some.txt"), "Hello world !", { encoding: 'utf-8' })
        console.log(API_BASE_PATH);
    })
