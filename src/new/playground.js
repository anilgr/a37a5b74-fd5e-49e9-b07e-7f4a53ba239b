const path = require("path");
const { PArray, parrayOf } = require("./parray");
const { API_BASE_PATH } = require("../globals");
const { knTokenize } = require("./util");
const { API } = require("./api");

// const rootFile = (fileName)=>path.join(API_BASE_PATH, fileName);
// parrayOf(...(PArray.deserialize("../../bk_data_3.txt").map(w=>w.trim()))).serialize("../../data_3.txt")
// parrayOf(...(PArray.deserialize("../../bk_data_4.txt").map(w=>w.trim()))).serialize("../../data_4.txt")
// parrayOf(...(PArray.deserialize("../../bk_data_5.txt").map(w=>w.trim()))).serialize("../../data_5.txt")

/* Group selected words into 3 4 and 5 letter words. */
// const words = parrayOf(parrayOf(), parrayOf(), parrayOf())
// PArray.deserialize(path.join(API_BASE_PATH, 'selected-words.txt')).forEach(w=>{
    // const l = knTokenize(w).length
    // words[l-3].push(w)
// })
// words.forEach(a=>a.push("-----------"))
// parrayOf(...words.flat()).serialize(path.join(API_BASE_PATH, 'selected-words-grped.txt'))

/* List words in api */
// const words = parrayOf()
// API.forEachRoute(({response})=>{
//     words.push(response.solution)
// })
// words.serialize(path.join(API_BASE_PATH, "api-words.txt"))

/* insert five letter words in between the current selected words. */
// const _5w = PArray.deserialize(rootFile('_5w.txt'));
// const selected = PArray.deserialize(rootFile('selected-words-grped.txt')).randomize()
// for(let i = 0; i < selected.length; i++) {
//     if(i%5 == 0 && i < selected.length - 1 ) {
//         selected.push(selected.splice(i, 1, _5w.pop()));
//     }
// }
// _5w.serialize(rootFile('a.txt'))
// selected.serialize(rootFile('b.txt'))

/* Randomize selected words */
const SELECTED_WORDS_PATH = path.join(API_BASE_PATH, 'selected-words.txt');
PArray.deserialize(SELECTED_WORDS_PATH).randomize().serialize(SELECTED_WORDS_PATH);


/* Export from Alar export json */
// const bm = require('./alar_export.json').bookmarks;
// PArray.from(bm.map(b=>b.word)).serialize("./exp-words.txt");
