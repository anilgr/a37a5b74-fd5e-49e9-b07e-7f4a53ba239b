const fs = require('fs')
const path = require('path')

const init = () => {

    Array.prototype.randomize = function () {
        this.forEach((v, i) => {
            const randomIndex = Math.floor(Math.random() * this.length)
            const temp = this[randomIndex];
            this[randomIndex] = v
            this[i] = temp;
        })
        return this;
    }

    Array.prototype.serialize = function (pathStr) {
        let data = ""
        this.forEach((v, i) => {
            data += v + "\n"
        })
        fs.writeFileSync(pathStr, data)
    }

    Array.deserialize = function (pathStr) {
        const filePath = path.join(__dirname, pathStr);
        let words = fs.readFileSync(filePath, 'utf8').trim().split('\n');
        return words || []
    }

    Date.prototype.format = function formatDateWithLeadingZeros() {
        const day = String(this.getDate()).padStart(2, '0');
        const month = String(this.getMonth() + 1).padStart(2, '0');
        const year = this.getFullYear();
        return `${year}/${month}/${day}`;
    }

}

init();