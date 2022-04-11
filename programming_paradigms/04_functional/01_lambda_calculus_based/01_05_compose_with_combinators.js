
let B = f => g => a => f(g(a));
let BL = f => g => a=> b => f(g(a)(b));

let inc = x => x + 1;

// bluebird offset
let blue_offset_by_3 = B(B(inc)(inc))(inc);
let result1 = blue_offset_by_3(1);
console.log(`Blue Result ${result1}`);

// blackbird offset
let black_offset_by_3 = BL(B)(B)(inc)(inc)(inc);
let result2 = black_offset_by_3(1);
console.log(`Black Result ${result2}`);
