const path = require('path');
const { API_BASE_PATH } = require('../globals');

function pathFromDate(date) {
    return path.join(API_BASE_PATH, date.toISOString().split('T')[0].split('-').join('\\')) + ".json";
}

// Thanks to vinayakakv https://github.com/vinayakakv/akshara_tokenizer
let swara = '[\u0c85-\u0c94\u0ce0\u0ce1]';
let vyanjana = '[\u0c95-\u0cb9\u0cde]';
let halant = '\u0ccd';
let vowel_signs = '[\u0cbe-\u0ccc]';
let anuswara = '\u0c82';
let visarga = '\u0c83';
let ardha_visarga = '\u0cbc'
let expression = new RegExp(`(?:(${swara})|((?:${vyanjana}${halant})*)(${vyanjana})(?:(${vowel_signs})|(${halant}))?)(${anuswara}|${visarga})?|\-`, 'g');

const swaraExp = new RegExp(`(${swara})`)
const vyanjanaExp = new RegExp(`(${vyanjana})`)
const vowel_signsExp = new RegExp(`(${vowel_signs})`)
const halantExp = new RegExp(`(${halant})`)
const anuswara_visargeExp = new RegExp(`(${anuswara}|${visarga})`)

const knTokenize = (mystring = "") => {
    return mystring.match(expression) || [];
}


module.exports = {
    pathFromDate,
    knTokenize
}