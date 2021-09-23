

let increment = x => x + 1;

let compose = f1 => f2 => arg => f1(f2(arg));

let offset_by_2 = compose(increment)(increment);
let result1 = offset_by_2(1);
console.log(`Result 1: ${result1}`);

let offset_by_4 = compose(
  compose(increment)(increment)
)(increment);
let result2 = offset_by_4(1);
console.log(`Result 2: ${result2}`);
