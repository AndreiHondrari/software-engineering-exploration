let B = (f) => (g) => (x) => f(g(x));

let b1 = B(
  (v) => {
    console.log("F called");
    return 11;
  },
)(
  (v) => {
    console.log("G called");
  },
);

let res = b1(99);
console.log(res);
