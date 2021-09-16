

let increment = x => x + 1;

// add + 1 + 1 + 1
let result = increment(increment(increment(1)));
console.log(`Result: ${result}`);
