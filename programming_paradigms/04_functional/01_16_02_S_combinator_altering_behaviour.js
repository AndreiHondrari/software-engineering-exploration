let I = (x) => x;
let K = (a) => ((b) => a);
let KI = (a) => ((b) => (b));

let T = (x) => K(x);
let F = (x) => KI(x);

let FIRST = (p) => p(T);
let SECOND = (p) => p(F);

let S = (f) => (g) => (z) => f(z)(g(z));

let g = (v) => {
  console.log("G call");
  return 999;
};

console.log("S(T)(g)");
let s1 = S(T)(g);
let res = s1(11);
console.log("s1 res:", res, "\n");

console.log("S(F)(g)");
let s2 = S(F)(g);
res = s2(11);
console.log("s2 res:", res, "\n");
