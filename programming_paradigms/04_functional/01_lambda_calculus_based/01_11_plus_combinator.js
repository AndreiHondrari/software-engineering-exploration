// Plus combinator

let ONCE = (f) => (x) => f(x);
let TWICE = (f) => (x) => f(f(x));

let PLUS = (m) => (n) => (f) => (x) => m(f)(n(f)(x));

let THRICE = PLUS(ONCE)(TWICE);

let add_one = (x) => x + 1;
let res = THRICE(add_one)(0);

/*
The PLUS combinator combines churchill numerators into a new composition
representing the sum of the joint applications
*/

console.log(res);
