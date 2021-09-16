
// BASIC DEFINITIONS

// the identity
// x.x
let I = x => x;

// the mockingbird - applies function on itself
// f.ff
let M = f => f(f);

// the kestrel - returns a function that returns the first parameter,
// ignores the second parameter
// ab.a
let K = (a) => ((b) => a);

// the kite - returns an identity, ignores first parameter,
// returns the second parameter if called upon
// ab.b
let KI = (a) => ((b) => (b));

// the cardinal - reverses the parameters for a given function
// fab.fba
// f => a => b => f(b)(a)
let C = (f) => (
  (a) => (
    (b) => f(b)(a)
  )
);

// TRUE
let T = (x) => K(x);

// FALSE
let F = (x) => KI(x);

// NOT
// also C
let NOT = (p) => p(F)(T);

// AND
let AND = (p) => ( (q) => p(q)(F) );
let ALT_AND = (p) => ( (q) => p(q)(p) );

// OR
let OR = (p) => ( (q) => p(T)(q) );
let ALT_OR = (p) => ( (q) => p(p)(q) );

// IF
let IF = (cond) => C(cond);

// EQ
let EQ = (a) => ( (b) => a(b(T)(F))(b(F)(T)) );
let ALT_EQ = (a) => ( (b) => a(b(a)(b))(b(a)(T)) );
let GATES_EQ = (a) => (b) => (
  OR (
    AND(a)(b)
  ) (
    AND(NOT(a))(NOT(b))
  )
)

// XOR
let XOR = (a) => (b) => a(b(F)(T))(b(T)(F));
let ALT_XOR = (a) => (b) => a(b(F)(a))(b(T)(b));
let GATES_XOR = (a) => (b) => (
  OR (
    AND(a)(NOT(b))
  )(
    AND(NOT(a))(b)
  )
);

// EXPERIMENTS

// I(I)
console.log("I(I): ", I(I) );

// M(I)
console.log("M(I): ", M(I) );

// K(I)
console.log("K(I): ", K(I) );

// (K(I))(123)
console.log("(K(I))(123): ", K(I)(123) );

// (K(M))(I)
console.log("(K(M))(I): ", K(M)(I) );

// (K(I))(M)
console.log("(K(I))(M): ", K(I)(M) );

// (K(111))(222) - select first
console.log("K 111 222 (select first): ", K(111)(222) );

// ((K(I))(111))(222)
console.log("K I 111 222 (select second): ", K(I)(111)(222) );

// K I M K
console.log("K I M K: ", K(I)(M)(K) );

// K I K M
console.log("K I K M: ", K(I)(K)(M) );

// C I - applies second as function over first
console.log("C I: ", C(I));

// C I 111
console.log("C I 111: ", C(I)(111));

// C I 111 I
console.log("C I 111 I: ", C(I)(111)(I));

// C K
console.log("C K: ", C(K));

// C K 111
console.log("C K 111: ", C(K)(111) );

// C K 111 I
console.log("C K 111 I: ", C(K)(111)(I) );

// C K 111 I
console.log("C K 111 I 222: ", C(K)(111)(I)(222) );

// C K M I
console.log("C K M I: ", C(K)(M)(I) );

// C K M I 111
console.log("C K M I 111: ", C(K)(M)(I)(111) );

// C K I M
console.log("C K I M: ", C(K)(I)(M) );

// NOT F
console.log("NOT F: ", NOT(F));

// C F
console.log("C F T F: ", C(F)(T)(F));

// NOT T
console.log("NOT T: ", NOT(T));

// NOT T
console.log("C T T F: ", C(T)(T)(F));

// AND
console.log("AND F F: ", AND(F)(F) );
console.log("AND F T: ", AND(F)(T) );
console.log("AND T F: ", AND(T)(F) );
console.log("AND T T: ", AND(T)(T) );

console.log("ALT_AND F F: ", ALT_AND(F)(F) );
console.log("ALT_AND F T: ", ALT_AND(F)(T) );
console.log("ALT_AND T F: ", ALT_AND(T)(F) );
console.log("ALT_AND T T: ", ALT_AND(T)(T) );

// OR
console.log("OR F F: ", OR(F)(F) );
console.log("OR F T: ", OR(F)(T) );
console.log("OR T F: ", OR(T)(F) );
console.log("OR T T: ", OR(T)(T) );

console.log("ALT_OR F F: ", ALT_OR(F)(F) );
console.log("ALT_OR F T: ", ALT_OR(F)(T) );
console.log("ALT_OR T F: ", ALT_OR(T)(F) );
console.log("ALT_OR T T: ", ALT_OR(T)(T) );

// IF
console.log("IF F 111 222: ", IF(F)(111)(222));
console.log("IF T 111 222: ", IF(T)(111)(222));

// EQ
console.log("EQ F F: ", EQ(F)(F) );
console.log("EQ F T: ", EQ(F)(T) );
console.log("EQ T F: ", EQ(T)(F) );
console.log("EQ T T: ", EQ(T)(T) );

console.log("ALT_EQ F F: ", ALT_EQ(F)(F) );
console.log("ALT_EQ F T: ", ALT_EQ(F)(T) );
console.log("ALT_EQ T F: ", ALT_EQ(T)(F) );
console.log("ALT_EQ T T: ", ALT_EQ(T)(T) );

console.log("GATES_EQ F F: ", GATES_EQ(F)(F) );
console.log("GATES_EQ F T: ", GATES_EQ(F)(T) );
console.log("GATES_EQ T F: ", GATES_EQ(T)(F) );
console.log("GATES_EQ T T: ", GATES_EQ(T)(T) );

// XOR
console.log("XOR F F: ", XOR(F)(F) );
console.log("XOR F T: ", XOR(F)(T) );
console.log("XOR T F: ", XOR(T)(F) );
console.log("XOR T T: ", XOR(T)(T) );

console.log("ALT_XOR F F: ", ALT_XOR(F)(F) );
console.log("ALT_XOR F T: ", ALT_XOR(F)(T) );
console.log("ALT_XOR T F: ", ALT_XOR(T)(F) );
console.log("ALT_XOR T T: ", ALT_XOR(T)(T) );

console.log("GATES_XOR F F: ", GATES_XOR(F)(F) );
console.log("GATES_XOR F T: ", GATES_XOR(F)(T) );
console.log("GATES_XOR T F: ", GATES_XOR(T)(F) );
console.log("GATES_XOR T T: ", GATES_XOR(T)(T) );

// De Morgan Law
// !(a & b) == !a || !b
let DE_MORGAN_IDENTITY = (a) => (b) => (
  EQ(
    NOT(
      AND(a)(b)
    )
  ) (
    OR(NOT(a))(NOT(b))
  )
)
console.log("DE_MORGAN_IDENTITY F F: ", DE_MORGAN_IDENTITY(F)(F) );
console.log("DE_MORGAN_IDENTITY F T: ", DE_MORGAN_IDENTITY(F)(T) );
console.log("DE_MORGAN_IDENTITY T F: ", DE_MORGAN_IDENTITY(T)(F) );
console.log("DE_MORGAN_IDENTITY T T: ", DE_MORGAN_IDENTITY(T)(T) );
