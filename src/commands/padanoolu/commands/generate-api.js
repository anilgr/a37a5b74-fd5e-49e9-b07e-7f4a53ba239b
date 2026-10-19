const fs = require('fs');
const path = require('path');
const { Command } = require('commander');
const { Route } = require('../../../core/route');
const {
    PADANOOLU_DATA_PATH,
    PADANOOLU_START_DATE,
} = require('../../../../config/default');

module.exports = new Command('generate-api')
    .description('Generate daily static JSON API for Padanoolu puzzles based on data/padanoolu/puzzles.txt')
    .option('--start-date <date>', 'Game start date (YYYY-MM-DD)', PADANOOLU_START_DATE)
    .option('--input <file>', 'Input puzzles file', PADANOOLU_DATA_PATH)
    .action((options) => {
        const inputPath = path.resolve(options.input);
        if (!fs.existsSync(inputPath)) {
            console.error(`Input file not found: ${inputPath}`);
            process.exit(1);
        }

        const rawContent = fs.readFileSync(inputPath, 'utf-8');
        const lines = rawContent.split('\n')
            .map(line => line.trim())
            .filter(line => line.length > 0 && !line.startsWith('#'));

        if (lines.length === 0) {
            console.log('No valid puzzle lines found in input file.');
            return;
        }

        const [startYear, startMonth, startDay] = options.startDate.split('-').map(Number);
        let currentDate = new Date(startYear, startMonth - 1, startDay);
        const defaultStartDate = `${startYear}/${String(startMonth).padStart(2, '0')}/${String(startDay).padStart(2, '0')}`;

        console.log(`Starting generation from ${options.startDate} for ${lines.length} puzzle(s)...`);

        let generatedCount = 0;

        lines.forEach((line, index) => {
            const parts = line.split('|');
            const themeHint = parts[0] || '';
            const wordsList = (parts[2] || '').split(',').map(w => w.trim()).filter(w => w.length > 0);
            const themeWord = wordsList[0] || parts[1] || '';

            const paths = parts.slice(3).map(pathStr => {
                return pathStr.split(';').map(coordStr => {
                    return coordStr.split(',').map(Number);
                });
            });

            const response = {
                id: `padanoolu_${index + 1}`,
                themeHint,
                themeWord,
                words: wordsList,
                paths,
                startDate: defaultStartDate,
            };

            // Saves to: <API_BASE_PATH>/api/padanoolu/<YYYY>/<MM>/<DD>.json
            const targetPath = Route.pathFromDate(currentDate, path.join('api', 'padanoolu'));
            const route = new Route(targetPath, response);
            route.saveToDisk();

            console.log(`[Generated] ${currentDate.toISOString().split('T')[0]} -> ${targetPath}`);

            // Increment to next day
            currentDate.setDate(currentDate.getDate() + 1);
            generatedCount++;
        });

        console.log(`\nSuccessfully generated ${generatedCount} Padanoolu daily puzzle API file(s).`);
    });
