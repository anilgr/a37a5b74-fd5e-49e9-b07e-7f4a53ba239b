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

const volwelToVowelMap = new Map();

volwelToVowelMap.set('ಅ', 'ಾ')
volwelToVowelMap.set('ಆ', 'ಾ')
volwelToVowelMap.set('ಇ', 'ಿ')
volwelToVowelMap.set('ಈ', 'ೀ')
volwelToVowelMap.set('ಉ', 'ು')
volwelToVowelMap.set('ಊ', 'ೂ')
volwelToVowelMap.set('ಋ', 'ೃ')
volwelToVowelMap.set('ಎ', 'ೆ')
volwelToVowelMap.set('ಏ', 'ೇ')
volwelToVowelMap.set('ಐ', 'ೈ')
volwelToVowelMap.set('ಒ', 'ೊ')
volwelToVowelMap.set('ಓ', 'ೋ')
volwelToVowelMap.set('ಔ', 'ೌ')
volwelToVowelMap.set('ಅಂ', '\u0c82')
volwelToVowelMap.set('ಅಃ', '\u0c83')

const diacriticToVowelMap = new Map();

diacriticToVowelMap.set('ಾ', 'ಅ')
diacriticToVowelMap.set('ಾ', 'ಆ')
diacriticToVowelMap.set('ಿ', 'ಇ')
diacriticToVowelMap.set('ೀ', 'ಈ')
diacriticToVowelMap.set('ು', 'ಉ')
diacriticToVowelMap.set('ೂ', 'ಊ')
diacriticToVowelMap.set('ೃ', 'ಋ')
diacriticToVowelMap.set('ೆ', 'ಎ')
diacriticToVowelMap.set('ೇ', 'ಏ')
diacriticToVowelMap.set('ೈ', 'ಐ')
diacriticToVowelMap.set('ೊ', 'ಒ')
diacriticToVowelMap.set('ೋ', 'ಓ')
diacriticToVowelMap.set('ೌ', 'ಔ')
diacriticToVowelMap.set('\u0c82', 'ಅಂ')
diacriticToVowelMap.set('\u0c83', 'ಅಃ')

// Kannada characters array
const kannadaAlphabet = [
    anuswara, visarga,
    'ಅ', 'ಆ', 'ಇ', 'ಈ', 'ಉ', 'ಊ', 'ಋ', 'ಎ', 'ಏ', 'ಐ', 'ಒ', 'ಓ', 'ಔ',// Vowels
    'ಕ', 'ಖ', 'ಗ', 'ಘ', 'ಙ', 'ಚ', 'ಛ', 'ಜ', 'ಝ', 'ಞ', 'ಟ', 'ಠ', 'ಡ', 'ಢ', 'ಣ',
    'ತ', 'ಥ', 'ದ', 'ಧ', 'ನ', 'ಪ', 'ಫ', 'ಬ', 'ಭ', 'ಮ', 'ಯ', 'ರ', 'ಲ', 'ವ', 'ಶ', 'ಷ', 'ಸ', 'ಹ', 'ಳ'
];

module.exports = {
    pathFromDate,
    knTokenize,
    diacriticToVowelMap,
    volwelToVowelMap,
    swaraExp,
    vyanjanaExp,
    halant,
    visarga,
    halantExp,
    kannadaAlphabet,
    anuswara_visargeExp
}