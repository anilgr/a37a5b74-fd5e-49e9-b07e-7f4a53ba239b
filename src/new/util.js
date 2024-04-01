const path = require('path');
const { API_BASE_PATH } = require('../globals');

function pathFromDate(date) {
    return path.join(API_BASE_PATH, date.toISOString().split('T')[0].split('-').join('\\')) + ".json";
}

module.exports = {
    pathFromDate
}