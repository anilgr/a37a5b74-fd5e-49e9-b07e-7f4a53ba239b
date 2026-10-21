const fs = require('fs');
const path = require('path');
const { execFile } = require('child_process');

function savePadanoolu(req, res, { parsedUrl, rootDir }) {
  let body = '';
  req.on('data', chunk => { body += chunk; });
  req.on('end', () => {
    try {
      const payload = JSON.parse(body || '{}');
      const content = payload.content;
      const targetFilename = payload.file === 'in_api' ? 'in_api_puzzles.txt' : 'puzzles.txt';

      if (typeof content !== 'string') {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: false, error: 'Missing content string' }));
        return;
      }

      // Ensure data/padanoolu directory exists
      const targetDir = path.join(rootDir, 'data', 'padanoolu');
      if (!fs.existsSync(targetDir)) {
        fs.mkdirSync(targetDir, { recursive: true });
      }

      // Write content to target file
      const targetFile = path.join(targetDir, targetFilename);
      fs.writeFileSync(targetFile, content, 'utf8');

      // Helper function to run git commands sequentially
      const runGit = (args) => new Promise((resolve, reject) => {
        execFile('git', args, { cwd: rootDir }, (error, stdout, stderr) => {
          if (error) {
            return reject(new Error((stderr || stdout || error.message).trim()));
          }
          resolve((stdout || stderr).trim());
        });
      });

      // Stage, commit, and push data/padanoolu/<targetFilename>
      (async () => {
        try {
          const relFilePath = path.posix.join('data', 'padanoolu', targetFilename);
          await runGit(['add', relFilePath]);

          // Only commit if there are staged changes
          let commitOutput = 'No changes to commit';
          try {
            commitOutput = await runGit(['commit', '-m', `Update Padanoolu ${targetFilename} data`]);
            console.log(`[Git Commit] ${commitOutput}`);
          } catch (commitErr) {
            if (commitErr.message.includes('nothing to commit')) {
              console.log('[Git Commit] Nothing to commit, working tree clean.');
            } else {
              throw commitErr;
            }
          }

          // Push to current branch remote
          const pushOutput = await runGit(['push']);
          console.log(`[Git Push] ${pushOutput}`);

          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ 
            success: true, 
            path: `data/padanoolu/${targetFilename}`,
            gitPushed: true,
            message: `Saved, committed, and pushed ${targetFilename} to GitHub!`
          }));
        } catch (gitErr) {
          console.error('[Git Error]', gitErr);
          // File was saved locally, but git operation encountered an issue
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ 
            success: true, 
            path: `data/padanoolu/${targetFilename}`,
            gitPushed: false,
            warning: `Saved ${targetFilename} locally, but Git push failed: ` + gitErr.message
          }));
        }
      })();
    } catch (err) {
      console.error('[HTTP 500] Error saving padanoolu puzzles:', err);
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ success: false, error: err.message }));
    }
  });
}

module.exports = {
  savePadanoolu,
};
