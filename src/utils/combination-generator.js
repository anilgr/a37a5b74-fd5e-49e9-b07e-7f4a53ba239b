// Function to generate combinations of `r` elements from an array of size `n`
function* generateCombinations(arr, r) {
    const n = arr.length;
    const indices = Array.from({ length: r }, (_, i) => i);

    while (true) {
        yield indices.map(i => arr[i]);

        let i = r - 1;
        while (i >= 0 && indices[i] === i + n - r) i--;

        if (i < 0) break;

        indices[i]++;
        for (let j = i + 1; j < r; j++) {
            indices[j] = indices[j - 1] + 1;
        }
    }
}

function createCombinationGenerator(toSelectFrom, count) {
    const combinationGenerator = generateCombinations(toSelectFrom, count);
    return {
        getNextCombination: function () {
            const next = combinationGenerator.next();
            return next.done ? null : next.value;
        }
    };
}

module.exports = {
    createCombinationGenerator,
}






