const { PArray, parrayOf } = require("./parray");
parrayOf(...(PArray.deserialize("../../bk_data_3.txt").map(w=>w.trim()))).serialize("../../data_3.txt")
parrayOf(...(PArray.deserialize("../../bk_data_4.txt").map(w=>w.trim()))).serialize("../../data_4.txt")
parrayOf(...(PArray.deserialize("../../bk_data_5.txt").map(w=>w.trim()))).serialize("../../data_5.txt")
