const padanoolu = require('./padanoolu');

// Map of "METHOD /pathname" -> handler(req, res, { parsedUrl, rootDir })
const routes = {
  'POST /api/save-padanoolu': padanoolu.savePadanoolu,
};

module.exports = routes;
