// Magic combinator (phi)

let I = (x) => x;
let K = (a) => ((b) => a);
let KI = (a) => ((b) => (b));

let T = (x) => K(x);
let F = (x) => KI(x);

let FIRST = (p) => p(T);
let SECOND = (p) => p(F);

let k1 = FIRST(I)(66)(77);
console.log("k1", k1);

let k2 = SECOND(I)(66)(77);
console.log("k2", k2);
