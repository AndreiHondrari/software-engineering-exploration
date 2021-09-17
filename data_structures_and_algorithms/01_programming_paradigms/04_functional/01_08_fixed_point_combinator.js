
// essentially a recursive combinator
// a function that calls itself infinitely
let Y = f => ( (x => f(x(x))) (x => f(x(x))) );

Y(() => {console.log("HAY");})
