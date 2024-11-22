const fs = require('fs')
const path = require('path')
const { API_BASE_PATH } = require('../globals')

class PArray extends Array {
    constructor(arrayLength) {
        super(arrayLength)
    }

    

    randomize() {
        this.forEach((v, i) => {
            const randomIndex = Math.floor(Math.random() * this.length)
            const temp = this[randomIndex];
            this[randomIndex] = v
            this[i] = temp;
        })
        return this;
    }

    serialize(pathStr) {
        let data = ""
        this.forEach((v, i) => {
            data += v + "\n"
        })
        fs.writeFileSync(pathStr, data)
        return this;
    }

    contains(value) {
        return this.indexOf(value) !== -1
    }

    static deserialize(pathStr) {
        let words = Array.from(new Set(fs.readFileSync(pathStr, 'utf8').trim().split('\n')))
        words = PArray.from(words);
        return words || new PArray(0)
    }

    static from(array) {
        let parray = new PArray(0)
        array.forEach(e=>parray.push(e))
        return parray;
    }
}

function parrayOf(...args) {
    args = args.flat()
    return PArray.from(args || [])
}

module.exports = {
    PArray,
    parrayOf
}