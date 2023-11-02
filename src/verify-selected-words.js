require("./extension_functions.js")
const words = Array.deserialize("../data.txt");
const selectedWords = Array.deserialize("../selected-words.txt")
const notFound = selectedWords.filter((w) => {
    console.log(words.indexOf(w.trim()))
    return words.indexOf(w.trim()) == -1
})
console.log(notFound)
if (notFound && notFound.length > 0)
    notFound.serialize("../selected-words-not-found.txt")