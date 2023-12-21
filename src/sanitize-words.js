require("./extension_functions")
const path = require('path')
const file = process.argv[2]
const filePath = path.join("../", file)
const words = Array.deserialize(filePath)
const mappedWords  = words.map((w)=>w.trim())
const wordsSet = Array.from(new Set(mappedWords));
wordsSet.serialize(filePath)