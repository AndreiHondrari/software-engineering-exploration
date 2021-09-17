let K = (a) => ((b) => a);
let KI = (a) => ((b) => (b));
let C = f => a => b => f(b)(a);
let B = f => a => b => f(a(b));

let FIRST = x => K(x);
let SECOND = x => KI(x);

let IF = x => B(C)(C)(x);


let x = FIRST;
let result1 = IF(x)(111)(222);
console.log(`Result 1: ${result1}`);

x = SECOND;
let result2 = IF(x)(333)(444);
console.log(`Result 2: ${result2}`);
