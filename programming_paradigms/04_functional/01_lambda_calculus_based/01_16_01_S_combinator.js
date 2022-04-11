let S = (f) => (g) => (z) => f(z)(g(z));

let s1 = S(
  // f body
  (p) =>
    (q) => {
      console.log("Calling F");
      return 11;
    },
)(
  // g body
  (v) => {
    console.log("calling G");
    return 33;
  },
);

let res = s1(77);
console.log(res);
