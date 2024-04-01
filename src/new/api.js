const { readApi } = require("./api_paths_iterator");
const { Route } = require("./route");

class API {
    static forEachRoute(callback) {
        const api = readApi();
        let v = api.next().value
        while (v) {
            callback(new Route(v).readFromDisk())
            v = api.next().value
        }
    }
}

module.exports = {
    API
}