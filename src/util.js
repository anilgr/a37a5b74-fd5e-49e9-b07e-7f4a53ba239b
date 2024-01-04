const fs = require('fs');
const path = require('path');

// Function to read files recursively
function getDate(isMin, dirPath) {
    let date;
    function readFilesRecursively(directoryPath) {
        const files = fs.readdirSync(directoryPath);

        for (const file of files) {
            const filePath = path.join(directoryPath, file);
            const stats = fs.statSync(filePath);

            if (stats.isDirectory()) {
                // Recursively read files in the subdirectory
                readFilesRecursively(filePath);
            } else {

                // console.log(`File: ${filePath}`);
                const dateMatch = filePath.match(/\d{4}\\\d{2}\\\d{2}/);
                if (dateMatch) {
                    const d = new Date(dateMatch[0].split('\\').join('-'));

                    if (!isMin && (!date || d.getTime() > date.getTime())) {
                        date = d
                    } else if (isMin && (!date || d.getTime() < date.getTime())) {
                        date = d
                    }
                }
                //   console.log(`Content:\n${fileContent}`);
            }
        }
    }
    readFilesRecursively(dirPath);
    if (!date) {
        date = new Date();
    } else {
        date.setDate(date.getDate() + (isMin ? 0 : 1))
    }
    return date;
}


function getWordsInApi() {

    // Function to get the number of days in a month for a given year
    function getDaysInMonth(year, month) {
        return new Date(year, month, 0).getDate();
    }

    const startDate = getDate(true, "../");
    console.log(startDate);
    let year = startDate.getFullYear();
    let month = startDate.getMonth() + 1;
    let day = startDate.getDate();

    const wordsInApi = []

    // Create the directory path in the format "year/month"
    let directoryPath = path.join(__dirname, `../${year}/${String(month).padStart(2, '0')}`);

    // Create the JSON file inside the directory
    let filePath = path.join(directoryPath, `${String(day).padStart(2, '0')}.json`);

    for (let i = 0; ; i++) {

        // Create the directory path in the format "year/month"
        directoryPath = path.join(__dirname, `../${year}/${String(month).padStart(2, '0')}`);

        // Create the JSON file inside the directory
        filePath = path.join(directoryPath, `${String(day).padStart(2, '0')}.json`);

        // Write the JSON data to the file
        try {
            const data = fs.readFileSync(filePath, 'utf-8');
            const word = JSON.parse(data).solution
            if (word != null)
                wordsInApi.push(word)
        } catch (e) {
            console.log("Done")
            return wordsInApi
        }


        // Increment the day and check if it exceeds the days in the current month
        day++;
        const daysInCurrentMonth = getDaysInMonth(year, month);
        if (day > daysInCurrentMonth) {
            day = 1;
            month++;
            if (month > 12) {
                month = 1;
                year++;
            }
        }
    }
}

// Function to get the number of days in a month for a given year
function getDaysInMonth(year, month) {
    return new Date(year, month, 0).getDate();
}

const VALID_DATE_REGEX = /[0-9]{4}-([0][0-9]|[1][0-2])-[0-9]{2}/g

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
    getDate,
    getWordsInApi,
    getDaysInMonth,
    VALID_DATE_REGEX,
    knTokenize
}

// console.log(getDate('./'))

// // Example usage:
// const parentDirectoryPath = path.join(__dirname, './');
// const d = getDate(parentDirectoryPath);
// console.log(d)
