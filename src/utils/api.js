const { readApi } = require("./api_paths_iterator");
const { PArray } = require("./parray");
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

    static getWords() {
        let words = []
        this.forEachRoute((route)=>{
            words.push(route.response.solution)
        })
        return PArray.from(words)
    }
}

module.exports = {
    API
}