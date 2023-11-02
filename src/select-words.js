function selectWords() {
  const inquirer = require('inquirer');
  require('./extension_functions.js')

  const PAGE_SIZE = 20; // Number of options to show per page
  let currentPage = 0;
  const paginatedOptions = [];
  const selectedOptions = []

  // Function to show the current page with options
  function showPage() {
    const currentOptions = paginatedOptions[currentPage];
    displayOptionsFromFile(currentOptions);
  }

  // Function to read options from file and display them as a paginated checkbox list
  function displayOptionsFromFile(options) {
    // Prompt the user to select multiple options from the current page
    inquirer
      .prompt([
        {
          type: 'checkbox',
          name: 'selectedOptions',
          message: `Choose options (Page ${currentPage + 1}/${paginatedOptions.length}):`,
          choices: options,
          loop: false,
          pageSize: 20
        },
        {
          type: 'list',
          name: 'next',
          message: 'what next ?',
          choices: ["continue", "commit"]
        }
      ])
      .then((answers) => {
        selectedOptions.push(answers.selectedOptions)
        const unselected = options.filter((v) => answers.selectedOptions.indexOf(v) == -1);
        paginatedOptions[currentPage] = unselected;
        console.log()
        if (answers.next == 'continue') {
          currentPage++;
          if (currentPage < paginatedOptions.length) {
            showPage();
          }
        } else if (answers.next == 'commit') {
          const trimmed = selectedOptions.flat().map(v => v.trim());
          paginatedOptions.flat().serialize('../words.txt')
          trimmed.serialize('../selected-words.txt')
        }

      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }

  options = Array.deserialize('../words.txt').randomize();

  for (let i = 0; i < options.length; i += PAGE_SIZE) {
    paginatedOptions.push(options.slice(i, i + PAGE_SIZE));
  }

  // Start displaying the options from the first page
  showPage();


}

module.exports = {
  selectWords
}

selectWords();