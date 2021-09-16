
let B = f => g => a => f(g(a));

let quadratic = x => x * x;
let quartic = B(quadratic)(quadratic);
let octic = B(quartic)(quadratic);

let x = 2;
console.log(`Input value: ${x}`);
console.log(`Quadratic: ${quadratic(x)}`);
console.log(`Quartic: ${quartic(x)}`);
console.log(`Octic: ${octic(x)}`);
