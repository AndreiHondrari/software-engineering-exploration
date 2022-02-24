let B = (f) => (g) => (x) => f(g(x));

let add = (a, b) => {
  return a + b;
};

let mul = (a, b) => {
  return a * b;
};

let add_10 = (v) => add(10, v);

let mul_2 = (v) => mul(2, v);

let res = B(add_10)(mul_2)(2);
console.log("* 2 , + 10 =", res);

res = B(mul_2)(add_10)(2);
console.log("+ 10 , * 2 =", res);
