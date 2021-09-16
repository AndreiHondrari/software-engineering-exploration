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
* the function is idempotent, or has referential transparency, meaning that for a given set of inputs, there will always be the same output, making the function deterministic
  * the input to output idempotence also allows for memoization as a further step in optimising the access to frequent values, calculating ones, memorising it somewhere, and then retrieving it as the same inputs occur
* since there is no data dependency between two functions, not being able to change non-local state, that makes the functions very good candidates for parallelism, being thread-safe. Thread unsafety comes with shared data whose access to must be restricted by various mechanisms (locks, semaphores, mutexes, etc.)


## Optimisation

When it comes to pure functions, compilers have techniques to optimise the execution of the code by doing certain transformations.

### Common-subexpression elimination

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

### Tail call elimination
