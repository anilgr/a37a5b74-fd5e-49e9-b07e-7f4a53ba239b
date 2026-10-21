const http = require('http');
const fs = require('fs');
const path = require('path');
const routes = require('./routes');

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
  // API Routes (Matched via routes map)
  // ---------------------------------------------------------------------------
  const routeKey = `${req.method} ${parsedUrl.pathname}`;
  const routeHandler = routes[routeKey];
  if (routeHandler) {
    routeHandler(req, res, { parsedUrl, rootDir: ROOT });
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
