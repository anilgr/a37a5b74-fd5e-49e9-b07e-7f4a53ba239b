class PDate extends Date {
    _supportedOps = [">", ">=", "<", "<=", "==", "==="]
    constructor(...args) {
        super(...args)
        this.setUTCHours(0);
        this.setUTCMinutes(0);
        this.setUTCSeconds(0);
        this.setUTCMilliseconds(0);
    }

    increment() {
        this.setDate(this.getDate() + 1)
        return this
    }

    decrement() {
        this.setDate(this.getDate() - 1)
        return this
    }

    is(op, otherPDate) {
        if (!this._supportedOps.includes(op)) {
            throw new Error(`Unsupported operation ${op} on the type PDate`)
        }
        switch (op) {
            case ">": return this.getTime() > otherPDate.getTime();
            case "<": return this.getTime() < otherPDate.getTime();
            case ">=": return this.getTime() >= otherPDate.getTime();
            case "<=": return this.getTime() <= otherPDate.getTime();
            case "==": return this.getTime() == otherPDate.getTime();
            case "===": return this.getTime() === otherPDate.getTime();
        }
    }

    equals(date) {
        return this.getTime() === date.getTime();
    }

    toString() {
        const day = String(this.getDate()).padStart(2, '0');
        const month = String(this.getMonth() + 1).padStart(2, '0');
        const year = this.getFullYear();
        return `${year}/${month}/${day}`;
    }
}

module.exports = {
    PDate
}