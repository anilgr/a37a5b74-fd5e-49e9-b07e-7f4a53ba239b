function generateAPI() {
  const fs = require('fs');
  const path = require('path');
  const { getDate, getDaysInMonth, VALID_DATE_REGEX } = require('./util')
  require('./extension_functions')
  // Get the current date
  // const currentDate = getDate(false, "./");
  const today = new Date();
  const tomorrow = new Date(today);
  tomorrow.setDate(today.getDate() + 1);

  let currentDate = today;
  // let currentDate = tomorrow;

  // let currentDate = getDate(false, "../");

  if (!!process.argv[2]) {
    if (process.argv[2].toString().match(VALID_DATE_REGEX)) {
      currentDate = new Date(process.argv[2])
      console.log("Will be generating api's from " + currentDate)
    } else {
      console.log("Please pass a valid date string (yyyy-mm-dd)")
    }
  }

  // const startDate = getDate(true, "./");
  const newYear = new Date(today)
  newYear.setDate(today.getDate() + 3);
  const startDate = newYear
  console.log(startDate);
  let year = currentDate.getFullYear();
  let month = currentDate.getMonth() + 1;
  let day = currentDate.getDate();

  // Read words from the data file
  // const dataFilePath = path.join(__dirname, 'data.txt');
  let words = Array.deserialize('../selected-words.txt')

  // Get the number of words to consider from command-line arguments
  const numberOfWordsToConsider = words.length; // Default to 5 if no argument is provided
  const wordsToWrite = words.slice(0, numberOfWordsToConsider);

  // Loop through the words to write array and create folders and files
  let wordsWritten = []
  for (let i = 0; i < wordsToWrite.length; i++) {
    const word = wordsToWrite[i].trim();

    if (!word) break;

    // Create the directory path in the format "year/month"
    const directoryPath = path.join(__dirname, `../${year}/${String(month).padStart(2, '0')}`);

    // Create the directory if it doesn't exist
    fs.mkdirSync(directoryPath, { recursive: true });

    // Create the JSON file inside the directory
    const filePath = path.join(directoryPath, `${String(day).padStart(2, '0')}.json`);

    // JSON data to be written to the file
    const jsonData = {
      startDate: startDate.format(),
      solution: word.trim()
    };

    // Write the JSON data to the file
    fs.writeFileSync(filePath, JSON.stringify(jsonData, null, 2));

    console.log(`Folder and file created successfully at path: ${filePath}`);

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

    wordsWritten.push(word);

    // Remove the word from the data file
    // removeWordFromFile(dataFilePath, word);
  }

  words = words.filter((v) => { return wordsWritten.indexOf(v) == -1 })
  console.log(words.length, wordsWritten.length)
  words.serialize('../selected-words.txt')

  // let apiWords = Array.deserialize('words-in-api.txt') || [];
  // apiWords = [...apiWords, ...wordsWritten]
  // apiWords.serialize('words-in-api.txt')

  console.log(`Words have been written to the files.`);

}
module.exports = {
  generateAPI
}

generateAPI();