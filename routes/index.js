const padanoolu = require('./padanoolu');
const padanantu = require('./padanantu');

// Map of "METHOD /pathname" -> handler(req, res, { parsedUrl, rootDir })
const routes = {
  'POST /api/save-padanoolu': padanoolu.savePadanoolu,
  'POST /api/save-padanantu': padanantu.savePadanantu,
};

module.exports = routes;
