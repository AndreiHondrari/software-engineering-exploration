
let B = f => g => a => f(g(a));

let inc = x => x + 1;

let offset_by_3 = B(B(inc)(inc))(inc);

let result = offset_by_3(1);

console.log(`Result ${result}`);
