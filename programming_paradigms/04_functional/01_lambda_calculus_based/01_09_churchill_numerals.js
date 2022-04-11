// Churchill numerals

let ZERO = (f) => (x) => x;
let ONCE = (f) => (x) => f(x);
let TWICE = (f) => (x) => f(f(x));
let THRICE = (f) => (x) => f(f(f(x)));

let add_one = (x) => x + 1;

let res = ZERO(add_one)(0);
console.log("zero applications", res);

res = ONCE(add_one)(0);
console.log("one application", res);

res = TWICE(add_one)(0);
console.log("two applications", res);

res = THRICE(add_one)(0);
console.log("three applications", res);
