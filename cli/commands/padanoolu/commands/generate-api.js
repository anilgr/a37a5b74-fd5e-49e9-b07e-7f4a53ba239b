const fs = require('fs');
const path = require('path');
const { Command } = require('commander');
const { Route } = require('../../../core/route');
const {
    PADANOOLU_DATA_PATH,
    PADANOOLU_START_DATE,
    PADANOOLU_IN_API_PATH,
} = require('../../../../config/default');

function formatDateKey(date) {
    const y = date.getFullYear();
    const m = String(date.getMonth() + 1).padStart(2, '0');
    const d = String(date.getDate()).padStart(2, '0');
    return `${y}-${m}-${d}`;
}

function parseDateKey(dateStr) {
    const [y, m, d] = dateStr.split('-').map(Number);
    return new Date(y, m - 1, d);
}

function getNextAvailableDate(inApiPath, fallbackStartDateStr) {
    if (fs.existsSync(inApiPath)) {
        const inApiRaw = fs.readFileSync(inApiPath, 'utf-8');
        const inApiLines = inApiRaw.split('\n')
            .map(l => l.trim())
            .filter(l => l.length > 0 && !l.startsWith('#'));

        const dates = [];
        for (const line of inApiLines) {
            let parts = line.split('|');
            const firstToken = (parts[0] || '').trim();
            if (firstToken === '1' || firstToken === '0' || firstToken === '✓' || firstToken.toLowerCase() === 'true' || firstToken.toLowerCase() === 'false') {
                parts = parts.slice(1);
            }
            const dateStr = (parts[0] || '').trim();
            if (/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
                dates.push(dateStr);
            }
        }

        if (dates.length > 0) {
            // Sort to find the latest recorded date
            dates.sort();
            const latestDate = parseDateKey(dates[dates.length - 1]);
            latestDate.setDate(latestDate.getDate() + 1);
            return latestDate;
        }
    }

    return parseDateKey(fallbackStartDateStr);
}

module.exports = new Command('generate-api')
    .description('Generate daily static JSON API from puzzles.txt, append to in_api_puzzles.txt, and consume (clear) puzzles.txt')
    .option('--start-date <date>', 'Game start date (YYYY-MM-DD); if omitted, continues from latest date in in_api_puzzles.txt')
    .option('--input <file>', 'Input puzzles file', PADANOOLU_DATA_PATH)
    .option('--output-in-api <file>', 'Output in_api_puzzles file', PADANOOLU_IN_API_PATH)
    .option('--no-consume', 'Do not consume (empty) the input puzzles.txt file')
    .action((options) => {
        const inputPath = path.resolve(options.input);
        if (!fs.existsSync(inputPath)) {
            console.error(`Input file not found: ${inputPath}`);
            process.exit(1);
        }

        const outInApiPath = path.resolve(options.outputInApi);
        const rawContent = fs.readFileSync(inputPath, 'utf-8');
        const lines = rawContent.split('\n')
            .map(line => line.trim())
            .filter(line => line.length > 0 && !line.startsWith('#'));

        if (lines.length === 0) {
            console.log(`No puzzles found to consume in ${inputPath}.`);
            return;
        }

        const isLineReviewed = (line) => {
            const firstToken = (line.split('|')[0] || '').trim();
            return firstToken === '1' || firstToken === '✓' || firstToken.toLowerCase() === 'true';
        };

        const reviewedLines = lines.filter(isLineReviewed);
        const unreviewedLines = lines.filter(l => !isLineReviewed(l));

        if (reviewedLines.length === 0) {
            console.log(`No reviewed puzzles (starting with 1|) found to consume in ${inputPath} (${unreviewedLines.length} unreviewed puzzle(s) skipped).`);
            return;
        }

        // Determine starting date
        let currentDate;
        if (options.startDate) {
            currentDate = parseDateKey(options.startDate);
        } else {
            currentDate = getNextAvailableDate(outInApiPath, PADANOOLU_START_DATE);
        }

        const [startYear, startMonth, startDay] = PADANOOLU_START_DATE.split('-').map(Number);
        const defaultStartDate = `${startYear}/${String(startMonth).padStart(2, '0')}/${String(startDay).padStart(2, '0')}`;

        console.log(`Consuming ${reviewedLines.length} reviewed puzzle(s) from ${inputPath} starting from date ${formatDateKey(currentDate)} (${unreviewedLines.length} unreviewed kept)...`);

        let generatedCount = 0;
        const newInApiLines = [];

        reviewedLines.forEach((line, index) => {
            let parts = line.split('|');
            const firstToken = (parts[0] || '').trim();
            if (firstToken === '1' || firstToken === '0' || firstToken === '✓' || firstToken.toLowerCase() === 'true' || firstToken.toLowerCase() === 'false') {
                parts = parts.slice(1);
            }
            const themeHint = parts[0] || '';
            const wordsList = (parts[2] || '').split(',').map(w => w.trim()).filter(w => w.length > 0);
            const themeWord = wordsList[0] || parts[1] || '';

            const paths = parts.slice(3).map(pathStr => {
                return pathStr.split(';').map(coordStr => {
                    return coordStr.split(',').map(Number);
                });
            });

            const dateStr = formatDateKey(currentDate);

            const response = {
                id: `padanoolu_${dateStr.replace(/-/g, '_')}`,
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

            console.log(`[Generated] ${dateStr} -> ${targetPath}`);

            const restOfLine = parts.join('|');
            newInApiLines.push(`0|${dateStr}|${restOfLine}`);

            // Increment to next day
            currentDate.setDate(currentDate.getDate() + 1);
            generatedCount++;
        });

        // Ensure target directory exists for in_api_puzzles.txt
        const outDir = path.dirname(outInApiPath);
        if (!fs.existsSync(outDir)) {
            fs.mkdirSync(outDir, { recursive: true });
        }

        // Append to in_api_puzzles.txt (or initialize with header if new)
        const inApiHeader = '# Reviewed|Date|ThemeHint|ThemeWord|WordsList|Paths...\n';
        if (!fs.existsSync(outInApiPath) || fs.readFileSync(outInApiPath, 'utf-8').trim().length === 0) {
            fs.writeFileSync(outInApiPath, inApiHeader + newInApiLines.join('\n') + '\n', 'utf-8');
        } else {
            let existing = fs.readFileSync(outInApiPath, 'utf-8');
            if (!existing.endsWith('\n')) existing += '\n';
            fs.writeFileSync(outInApiPath, existing + newInApiLines.join('\n') + '\n', 'utf-8');
        }
        console.log(`[Appended] Added ${newInApiLines.length} puzzle(s) to ${outInApiPath}`);

        // Consume reviewed puzzles from input puzzles.txt file, keeping any unreviewed ones
        if (options.consume !== false) {
            const puzzlesHeader = '# Reviewed|ThemeHint|ThemeWord|WordsList|Paths...\n';
            const remainingBody = unreviewedLines.length > 0 ? unreviewedLines.join('\n') + '\n' : '';
            fs.writeFileSync(inputPath, puzzlesHeader + remainingBody, 'utf-8');
            console.log(`[Consumed] Removed ${reviewedLines.length} reviewed puzzle(s) from ${inputPath} (${unreviewedLines.length} unreviewed remaining)`);
        }

        console.log(`\nSuccessfully processed and generated ${generatedCount} Padanoolu daily puzzle API file(s).`);
    });
