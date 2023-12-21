require("./extension_functions.js")
const words_3 = Array.deserialize("../words_3.txt");
const words_4 = Array.deserialize("../words_4.txt");
const selectedWords = Array.deserialize("../selected-words.txt")
const notFound = selectedWords.filter((w) => {
    let i = words_3.indexOf(w.trim())
    let j = words_4.indexOf(w.trim())

    isNotFound =  i == -1 && j == -1
    if(!isNotFound) {
        if(i !== -1) {
            words_3.splice(i, 1);
        } else if(j !== -1) {
            words_4.splice(j, 1)
        }
    }
    return isNotFound
})
console.log(notFound)
if (notFound && notFound.length > 0)
    notFound.serialize("../selected-words-not-found.txt")

words_3.serialize('../words_3.txt')
words_4.serialize('../words_4.txt')