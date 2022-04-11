// Successor combinator

let TWICE = (f) => (x) => f(f(x));

let SUCC = (n) => (f) => (x) => f(n(f)(x));

let THRICE = SUCC(TWICE);

let add_one = (x) => x + 1;
let res = THRICE(add_one)(0);

/*
The successor combinator transforms the churchill numeral twice into
a thrice numeral, essentially allowing us to apply the
parameter function +1 more times
*/

console.log(res);
