const { API_BASE_PATH } = require("../globals");
const fs = require('fs');
const path = require('path');

function* readApi(dir = API_BASE_PATH) {
    const files = fs.readdirSync(dir).map(f => path.join(dir, f))
    let file = files.shift()
    while (file) {
        if (fs.statSync(file).isDirectory()) {
            files.push(...fs.readdirSync(file).map(f => path.join(file, f)))
        } else {
            const match = file.match(/\d{4}\\\d{2}\\\d{2}/);
            if (match) {
                yield file
            }
        }
        file = files.shift();
    }
}

module.exports = { readApi }