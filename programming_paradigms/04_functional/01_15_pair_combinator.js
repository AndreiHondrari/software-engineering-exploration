// Magic combinator (phi)

let I = (x) => x;
let K = (a) => ((b) => a);
let KI = (a) => ((b) => (b));

let PAIR = (a) => (b) => (f) => f(a)(b);

let pair_1 = PAIR(11)(22);

let res = pair_1((a) => (b) => a + b);
console.log(res);
