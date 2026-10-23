const fs = require('fs');
const path = require('path');
const { Command } = require('commander');
const { Route } = require('../../../core/route');
const {
    PADANOOLU_START_DATE,
    PADANOOLU_IN_API_PATH,
} = require('../../../../config/default');

module.exports = new Command('update')
    .description('Update daily static JSON API for Padanoolu puzzles based on data/padanoolu/in_api_puzzles.txt')
    .option('--input <file>', 'Input in_api_puzzles file', PADANOOLU_IN_API_PATH)
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

        const [defaultStartYear, defaultStartMonth, defaultStartDay] = PADANOOLU_START_DATE.split('-').map(Number);
        const defaultStartDate = `${defaultStartYear}/${String(defaultStartMonth).padStart(2, '0')}/${String(defaultStartDay).padStart(2, '0')}`;

        console.log(`Updating Padanoolu API from ${inputPath} for ${lines.length} puzzle(s)...`);

        let updatedCount = 0;

        lines.forEach((line, index) => {
            let parts = line.split('|');
            const firstToken = (parts[0] || '').trim();
            if (firstToken === '1' || firstToken === '0' || firstToken === '✓' || firstToken.toLowerCase() === 'true' || firstToken.toLowerCase() === 'false') {
                parts = parts.slice(1);
            }
            if (parts.length < 4) {
                console.warn(`[Skip] Invalid line format (expected [Reviewed|]Date|ThemeHint|ThemeWord|WordsList|Paths...): ${line}`);
                return;
            }

            const dateStr = parts[0].trim();
            if (!/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
                console.warn(`[Skip] Invalid date format "${dateStr}" at line ${index + 1}`);
                return;
            }

            const [year, month, day] = dateStr.split('-').map(Number);
            const puzzleDate = new Date(year, month - 1, day);

            const themeHint = parts[1] || '';
            const wordsList = (parts[3] || '').split(',').map(w => w.trim()).filter(w => w.length > 0);
            const themeWord = wordsList[0] || parts[2] || '';

            const paths = parts.slice(4).map(pathStr => {
                return pathStr.split(';').map(coordStr => {
                    return coordStr.split(',').map(Number);
                });
            });

            // Keep existing startDate if file already exists on disk, otherwise default
            const targetPath = Route.pathFromDate(puzzleDate, path.join('api', 'padanoolu'));
            let existingStartDate = defaultStartDate;
            if (fs.existsSync(targetPath)) {
                try {
                    const existingData = JSON.parse(fs.readFileSync(targetPath, 'utf-8'));
                    if (existingData.startDate) {
                        existingStartDate = existingData.startDate;
                    }
                } catch {
                    // Ignore parse error, use default
                }
            }

            const response = {
                id: `padanoolu_${dateStr.replace(/-/g, '_')}`,
                themeHint,
                themeWord,
                words: wordsList,
                paths,
                startDate: existingStartDate,
            };

            const route = new Route(targetPath, response);
            route.saveToDisk();

            console.log(`[Updated] ${dateStr} -> ${targetPath}`);
            updatedCount++;
        });

        console.log(`\nSuccessfully updated ${updatedCount} Padanoolu daily puzzle API file(s).`);
    });
