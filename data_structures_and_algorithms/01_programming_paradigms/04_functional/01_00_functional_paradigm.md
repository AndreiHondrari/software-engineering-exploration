# Functional Programming Paradigm

## Keywords
* first-class functions
* higher-order functions
  * map
  * filter
  * fold
  * sort
  * apply
  * partial application
  * function composition
  * currying
  * integration
  * callback
  * successor function
* pure functions
  * side effects
  * purity vs impurity; non-state but pure computation
  * deterministic vs non-deterministic algorithms
  * idempotence
  * memoization
  * parallelism and thread-safety
* recursion
  * tail call optimisation
* strict vs non-strict evaluation
* type systems
* referential transparency
* data structures -> "persistent" data structures


## Overview

Functional programming is a step forward from procedural sequences,
state changing and side effects creating via imperative statements.

Functional programming has the following characteristics:
* uses only immutable data
* functionality exist only in functions, not procedures or methods
* since all data is immutable, functions are all about transforming inputs to outputs, creating altered copies of the inputs
* storing data in some sort of linked nodes memory structures, like trees, that has values in the leaf nodes and references in intermediary non-leaf nodes.
* `(!)` functions operate on persistent data structures copying the minimum amount of nodes and referencing the existing ones that were not altered, in the process keeping an optimum amount of items and not wasting memory
* makes use of bridges that connects pure functionality that operates on immutable data, to impure, state-changing, side-effect producing code, that represents the desirable and practical outcome of our functionality. You can't have only pure functional programs because it would be a very complex machine that does a lot of useless things. Impurity is essential for programs to perform something useful.


## Concepts

### First-class functions

The idea of first-class function was already observed in procedural programming and the characteristics of these functions are:
* ability to assign functions to variables or data structures
* ability to be passed to functions as parameters
* ability for functions to be returned from other functions

Assigning functions to variables and data structures (Python)
```Python
def some_function():
  ...

# assign the function to a variable
some_variable = some_function

# use the function through the variable
some_variable()
```

```Python
def some_function():
  ...

some_dictionary = {
  x: 11,
  y: 22
}

# store the function in a dictionary
some_dictionary['do_something'] = some_function

# call the function from the dictionary
some_dictionary['do_something']()
```

Passing function to another function (Python):

```Python
def function_one():
  ...

def function_two(some_function):
  ...

function_two(function_one)
```

Returning a function from a function (Python):

```Python
def function_one():
  ...

def function_two():
  return function_one

# retrieve the function from a function
some_variable = function_two()

# call the retrieved function
some_variable()
```

Creating a function within a function (Python):

```Python
def retrieve_a_closure():
  def new_function():
    ...

  return new_function

closure = retrieve_a_closure()
closure()
```

### Higher-order functions

Higher-order functions are tightly connected to first-order functions, in the sense that higher-order functions are related to mathematics whereas first-order functions are tied to programming.

The most important characteristics of the high-order functions which distinguish them from all other first-order functions are:
* ability to receive functions as parameters
* ability to return functions

### Pure functions

Purity and impurity is a characteristic based on various factors:
* the function does not have side-effects:
  * no change of non-local variables (or non-local state, e.g. global)
  * no change of local variables (or local state)
  * no change of IO state
  * no change of referenced arguments
* the function is idempotent, meaning that for a given set of inputs, there will always be the same output, making the function deterministic
  * the input to output idempotence also allows for memoization as a further step in optimising the access to frequent values, calculating ones, memorising it somewhere, and then retrieving it as the same inputs occur
* since there is no data dependency between two functions, not being able to change non-local state, that makes the functions very good candidates for parallelism, being thread-safe. Thread unsafety comes with shared data whose access to must be restricted by various mechanisms (locks, semaphores, mutexes, etc.)

### Referential transparency

Refers to the avoidance of changing or depending on non-local state, making the function deterministic.

Referential transparent:
```Python
def do_something(x):
  return x + 5
```

```text
a == b
do_something(a) == do_something(b)
```

Referential opaque:
```Python
k = 1
def do_something(x):
  k = k + 1
  return x + k
```

```text
a == b
do_something(a) != do_something(b)
```

### Recursion

All loops (for/while) found in imperative languages are replaceable by recursive functions in functional programming as long as the recursion makes use of the tail-call optimisation.

Contrary to procedural recursive calls, which create a new frame for each level of recursive call, in functional programming it is necessary to make use of tail call optimisation, where the compiler recognises the existence of a recursive tail call and creates only one stack frame, hence the function can run infinitely without ever running into a stack overflow. You may think that this could be a problem, especially because each stack frame was a snapshot of each run of the function, memorising the local state being operated with, which is only a problem in a stateful algorithm, but if the algorithm relies solely on immutable data, mapping inputs to outputs, then at the machine code level, the only sequence of operations needed are calculation, replace parameters, jump to beginning of the function.

Example of non-tail call
```Python
def sum_up_to(x):
  return 0 if x == 0 else (sum_up_to(x - 1) + x)
```

Execution visualisation of this non-tail call (for `sum_up_to(4)`):
```
call sum_up_to(4)
  call sum_up_to(3)
    call sum_up_to(2)
      call sum_up_to(1)
        call sum_up_to(0)
        return 10
      return 10
    return 10
  return 10
return 10
```

Example of tail call
```Python
def sum_up_to(x, amount):
  return amount if x == 0 else sum_up_to(x - 1, amount + x)
```

Execution visualisation of this tail call (for `sum_up_to(4, 0)`):

```
call sum_up_to(4, 0)
  replace args with 3, 4
  jump to sum_up_to
  replace args with 2, 7
  jump to sum_up_to
  replace args with 1, 9
  jump to sum_up_to
  replace args with 0, 10
  jump to sum_up_to
  return 10
return 10
```

### Common-subexpression elimination
In the case of pure functions the compiler can do some extra optimisations like the common-subexpression elimination.

If the compiler detects two expressions like:
```C
x = a * b + p;
y = a * b + q;
```

then the compiler will notice the common `a * b` subexpression and will avoid performing the same operation twice by storing it:
```C
tmp = a * b;
x = tmp + p;
y = tmp + q;
```

## Currying

Instead of calling a function with multiple arguments, call it subsequently with one argument at a time.

Normal function:
```JS
function do_something(a, b, c) {
  return a + b + c;
}
do_something(1, 2, 3);
```

Curried function:
```JS
let do_something = (a) => (
  (b) => (
    (c) => a + b +c
  )
);

do_something(1)(2)(3);
```

or shorthand definition
```JS
let do_something = a => b => c => a + b + c;
```

## λ-calculus

Since a function is curried this opens the door to λ-calculus, which is a form of mathematics that deals with functions and their composition.

The possibility of doing function composition stems from the fact that a curried function accepts only one parameter at a time. Composition works by:
`(f•g)(x) = f(g(x))` essentially mapping the output of `g(x)` to `f(x)`. The composition itself represents a new operation.

Let's assume we have an incrementer function:
```JS
let increment = x => x + 1;
```

then it's composition of three times

```JS
increment(increment(increment(1)))
```

results in 3.

We can save this operation under a different name, but before we need to define a compose function that applies one function to another:

```JS
let compose = f1 => f2 => arg => f1(f2(arg));
let offset_by_2 = compose(increment)(increment);
offset_by_2(1)  // shows 3
```

or we can compose even further (`f1•f2•f3 = f1(f2(f3))`):
```JS
let offset_by_3 = compose( compose(increment)(increment) )(increment);
```
or
```JS
let offset_by_3 = compose(offset_by_2)(increment);
```

### Combinators

In lambda calculus there is the term of combinator, which is a function that has no free variables. Free variables are variables that exist in the body of the function, but are not bound via the arguments.

#### Types of combinators

##### I. Identity combinator - return itself

Form `I := λx.x`

```JS
let I = x => x;
```

##### M. Mockingbird combinator - apply on itself

Form `M := λf.ff` alternatively `f(f)`

```JS
let M = f => f(f);
```

##### K. Kastrel combinator - use the first, ignore the second

Form `K := λab.a`

```JS
let K = a => b => a;
```

##### KI. Kite combinator - ignore the first, use the second

Form `KI := λab.b`

```JS
let KI = a => b => b;
```

##### C. Cardinal combinator - the parameter flip

Form `C := λfab.fba` alternatively `f(b)(a)`

```JS
let C = f => a => b => f(b)(a);
```

##### B. Bluebird combinator - aplies arg to second function and then to the first

Form `B := λfab.f(ab)` alternatively `f(a(b))`

```JS
let B = f => a => b => f(a(b))
```

##### T. Thrush combinator - calls second with first as param

Form `T := λab.ba`

```JS
let T = a => b => b(a);
```

##### V. Vireo combinator

Form `V := λabf.fab`

```JS
let V = a => b => f => f(a)(b);
```

#### BL. Blackbird combinator

Form `BL := λfgab.f(gab)`

```JS
let BL = f => g => a => b => f(g(a)(b));
```

#### S. Starling combinator

Form `S := λabc.ac(bc)`

```JS
let S = a => b => c => a(c)(b(c));
```

### Some pragmatic examples of λ-calculus combinators

Now that we've defined some fundamental combinators, let's see what we can do with them.

It seems that our compose function is actually the equivalent of the **B combinator**.

```JS
let offset_by_3 = B(B(increment)(increment))(increment);
```

Exponents:
```JS
let quadratic = x => x * x;
let quartic = B(quadratic)(quadratic);
let octic = B(quartic)(quadratic);
```

Conditionals:

```JS
let FIRST = K;
let SECOND = KI;
p = // ... FIRST or SECOND
let IF = C(p)(111)(222);
```
