require("./extension_functions.js")
Array.deserialize("../selected-words.txt").randomize().serialize("../selected-words.txt")