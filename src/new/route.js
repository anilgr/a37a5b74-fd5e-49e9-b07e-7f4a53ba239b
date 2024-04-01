const fs = require('fs')
const path = require('path')
const { API_BASE_PATH } = require('../globals');

class Route {

    constructor(routePath, response = {}) {
        this.setPath(routePath)
        this.response = response;
    }

    readFromDisk() {
        const data = fs.readFileSync(this.path, 'utf-8');
        this.response = JSON.parse(data) || {}
        return this
    }

    setPath(routePath = __dirname + '\\default') {
        if (!routePath.startsWith(API_BASE_PATH)) {
            throw (`path base must be ${__dirname}`)
        }
        this.path = routePath
    }

    editResponse(editCallback) {
        const edit = editCallback(this.response)
        this.response = edit
    }

    saveToDisk() {
        const dirname = path.dirname(this.path);
        if (!fs.existsSync(dirname)) {
            fs.mkdirSync(dirname, { recursive: true });
        }
        fs.writeFileSync(this.path, JSON.stringify(this.response, null, 2), {})
    }
}

module.exports = {
    Route
}