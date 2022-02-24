// Multiplication combinator

let TWICE = (f) => (x) => f(f(x));
let THRICE = (f) => (x) => f(f(f(x)));

let MULT = (m) => (n) => (f) => m(n(f));

let SENCE = MULT(TWICE)(THRICE); // 2 * 3 = 6 (times)

let add_one = (x) => x + 1;
let res = SENCE(add_one)(0); // should be applied

/*
The MULT combinator combines churchill numerators into a new composition
representing the product of the joint applications
*/

console.log(res);
