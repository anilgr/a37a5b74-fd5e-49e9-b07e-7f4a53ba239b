const http = require('http');
const fs = require('fs');
const path = require('path');
const { execFile } = require('child_process');

// Port to listen on (defaults to 8080 or process.env.PORT)
const PORT = process.env.PORT || 8080;

// Root directory for serving files (daily-challenge-words-server root)
const ROOT = __dirname;

// Content types mapped to file extensions for static serving
const MIME_TYPES = {
  '.json': 'application/json',
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.txt': 'text/plain',
};

const server = http.createServer((req, res) => {
  // CORS headers so local web / apps can connect without origin issues
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', '*');

  // Handle CORS preflight requests
  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);

  // ---------------------------------------------------------------------------
  // API Routes
  // ---------------------------------------------------------------------------

  // POST /api/save-padanoolu: Save padanoolu puzzles content directly to data/padanoolu/puzzles.txt
  if (req.method === 'POST' && parsedUrl.pathname === '/api/save-padanoolu') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const payload = JSON.parse(body || '{}');
        const content = payload.content;

        if (typeof content !== 'string') {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ success: false, error: 'Missing content string' }));
          return;
        }

        // Ensure data/padanoolu directory exists
        const targetDir = path.join(ROOT, 'data', 'padanoolu');
        if (!fs.existsSync(targetDir)) {
          fs.mkdirSync(targetDir, { recursive: true });
        }

        // Write content to puzzles.txt
        const targetFile = path.join(targetDir, 'puzzles.txt');
        fs.writeFileSync(targetFile, content, 'utf8');

        // Helper function to run git commands sequentially
        const runGit = (args) => new Promise((resolve, reject) => {
          execFile('git', args, { cwd: ROOT }, (error, stdout, stderr) => {
            if (error) {
              return reject(new Error((stderr || stdout || error.message).trim()));
            }
            resolve((stdout || stderr).trim());
          });
        });

        // Stage, commit, and push data/padanoolu/puzzles.txt
        (async () => {
          try {
            await runGit(['add', 'data/padanoolu/puzzles.txt']);

            // Only commit if there are staged changes
            let commitOutput = 'No changes to commit';
            try {
              commitOutput = await runGit(['commit', '-m', 'Update Padanoolu puzzles data']);
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
              path: 'data/padanoolu/puzzles.txt',
              gitPushed: true,
              message: 'Saved, committed, and pushed to GitHub!'
            }));
          } catch (gitErr) {
            console.error('[Git Error]', gitErr);
            // File was saved locally, but git operation encountered an issue
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ 
              success: true, 
              path: 'data/padanoolu/puzzles.txt',
              gitPushed: false,
              warning: 'Saved locally, but Git push failed: ' + gitErr.message
            }));
          }
        })();
      } catch (err) {
        console.error('[HTTP 500] Error saving padanoolu puzzles:', err);
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: false, error: err.message }));
      }
    });
    return;
  }

  // ---------------------------------------------------------------------------
  // Static File Serving
  // ---------------------------------------------------------------------------

  // Sanitize path to prevent directory traversal
  let safePath = path.normalize(decodeURIComponent(parsedUrl.pathname)).replace(/^(\.\.[\/\\])+/, '');
  
  // Default root '/' to index.html
  if (safePath === '/' || safePath === '\\' || safePath === '') {
    safePath = 'index.html';
  }
  let filePath = path.join(ROOT, safePath);

  // Verify file existence and handle directories by searching for index.html
  fs.stat(filePath, (err, stats) => {
    if (!err && stats.isDirectory()) {
      filePath = path.join(filePath, 'index.html');
    }

    fs.stat(filePath, (err2, stats2) => {
      if (err2 || !stats2.isFile()) {
        console.log(`[HTTP 404] ${req.method} ${parsedUrl.pathname}`);
        res.writeHead(404, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Not Found', path: parsedUrl.pathname }));
        return;
      }

      // Stream the requested file with correct MIME type
      const ext = path.extname(filePath).toLowerCase();
      const contentType = MIME_TYPES[ext] || 'application/octet-stream';
      console.log(`[HTTP 200] ${req.method} ${parsedUrl.pathname}`);
      res.writeHead(200, { 'Content-Type': contentType });
      fs.createReadStream(filePath).pipe(res);
    });
  });
});

// Start the HTTP server
server.listen(PORT, '0.0.0.0', () => {
  console.log(`[daily-challenge-words-server] Serving static files from ${ROOT}`);
  console.log(`[daily-challenge-words-server] Running at http://localhost:${PORT}`);
});
