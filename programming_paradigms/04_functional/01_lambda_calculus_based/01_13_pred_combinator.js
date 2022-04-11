let I = (x) => x;

let TWICE = (f) => (x) => f(f(x));

let PRED = (n) => (f) => (x) => n((g) => (h) => h(g(f)))(() => x)(I);

let ONCE = PRED(TWICE);

let add_one = (v) => v + 1;

let original = TWICE(add_one)(0);
let res = ONCE(add_one)(0);

console.log(original);
console.log(res);
