require("./extension_functions")
const path = require('path')
const file = process.argv[2]
const filePath = path.join("../", file)
const words = Array.deserialize(filePath)
words.map((w)=>w.trim()).serialize(filePath)