const { halantExp, diacriticToVowelMap, anuswara_visargeExp } = require("./utils/util");

const firstNormalizeWord = (word)=>{
    return word.split("").filter(char => !(halantExp.test(char))).map(char=>((diacriticToVowelMap.has(char) && !anuswara_visargeExp.test(char)) ? diacriticToVowelMap.get(char) : char) ).sort().join("")
}

const normalizeWord = (word) => {
    return Array.from(new Set(firstNormalizeWord(word).split(""))).sort().join("")
}

class TrieNode {
    constructor() {
        this.children = {};
        this.isEndOfWord = false; // Flag to indicate end of a valid word
        this.words = [];           // Count of how many times this node is part of an inserted word
    }

    get count() {
        return this.words.length;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    // Insert a word into the trie
    insert(word) {
        let node = this.root;
        const condensedWord = normalizeWord(word);
        for (let char of condensedWord) {
            if (!node.children[char]) {
                node.children[char] = new TrieNode();
            }
            node = node.children[char];
        }
        node.isEndOfWord = true; // Mark the end of the word
        node.words.push(word);            // Increment the count at the end of the word
    }

    // Get the total count of words that end at nodes along the given path
    getTotalWordsOnPath(condensedWordPath = "", hasChar = "") {
        let node = this.root;
        let totalWordCount = 0;

        // Traverse the Trie along the path
        let doesHaveChar = false;
        for (let char of condensedWordPath) {
            if (!node.children[char]) {
                return totalWordCount; // Path does not exist, return the accumulated count
            }
            node = node.children[char];
            doesHaveChar = doesHaveChar ? true : char.startsWith(hasChar); 

            // Add count of words ending at this node
            if (node.isEndOfWord && doesHaveChar) {
                totalWordCount += node.count;
            }
        }

        return totalWordCount; // Return the total count of words that end along the path
    }
    
    getWords(condensedWord = "") {
        let node = this.root;
        for (let char of condensedWord) {
            if (!node.children[char]) {
                return [];
            }
            node = node.children[char];
        }
        return node.words;
    }
    
    getWordsCount(condensedWord = "") {
        let node = this.root;
        for (let char of condensedWord) {
            if (!node.children[char]) {
                return 0;
            }
            node = node.children[char];
        }
        return node.count;
    }
}

module.exports = {
    Trie,
    normalizeWord, 
    firstNormalizeWord
}


// const wordsInTrie = PArray.deserialize("words_data.txt").filter(w=>normalizeWord(w) === "ಅನ");

// console.log(wordsInTrie)

// console.log(trie.root.children["ಅ"].children["ನ"].children["ಮ"].children["ಷ"].count)

// console.log(trie.getTotalWordsOnPath("ಅನಮಷ")) // 0
