# Procedural programming paradigm

## Overview

Looking back to the imperative and structured programming paradigms we can
notice that even though we were able to reduce the repetition of some
sequences of instructions, the fact is that it is not enough in cases where
the code is duplicated in different programs, or in two different locations
in the sequence, or under different branches of execution flow that are
triggered by completely different circumstances.

Given:

```C
if (condition_1) {
  instruction_1;
}
else {
  instruction_x;
  instruction_y;
}

instruction_2;
instruction_3;

if (condition_2) {
  instruction_x;
  instruction_y;
}
```

we observe that the sequence `instruction_x; instruction_y;` is repeated in two different places. It would be ideal if we could place these somewhere unique and be able to execute the instructions at this place and then come back to our original execution flow. In low level programming this is possible using jump operations, but we are not using low level operations, and in high level operations there was the notion of `goto` that was deemed problematic by the illustrious dutch computer scientist Edsger Dijkstra.

The problem with jump and goto operations is that they are very atomic and one way, and you need an overlaying structure or protocol that enables one to go to a block of instructions, execute them, and then return to the origin of the jump/goto call. This sort of structure or protocol is called a **routine**, **subroutine**, **function** or **procedure**.

> The subroutine was first mentioned by Alan Turing in 1945 as "bury" and "unbury" operations of entering and exiting a subroutine. The concept of subroutine was pioneered by John Mauchly in 1947. In 1951 David Wheeler, Maurice Wilkes and Stanley Gill created a protocol of entering and exiting from a subroutine by memorizing the address for return, which was called "Wheeler jump".

Now let's rewrite that previous example using procedures:
```C
void perform_instructions() {
  instruction_x;
  instruction_y;
}

if (condition_1) {
  instruction_1;
}
else {
  perform_instructions();
}

instruction_2;
instruction_3;

if (condition_2) {
  perform_instructions();
}
```

Great! Now we can write once a massive sequence and call it via a simple call instruction.

These procedures open up the possibilities for new ways of structuring and thinking about code.

## Usages

You can call procedures from essentially a myriad of locations:
* if/else blocks
* loops
* other procedures
* other modules

## Properties of procedures

Procedures come along with a set of characteristics:
* local scope
* global scope
* inputs (arguments) and outputs (return values)
* reusability
* modularity

### Local scope

Every time you call a procedure the procedure can declare variables within itself and when this happens those variables lives start and end within the scope of that procedure, not leaking to the caller.

That also means that the variables in the scope of the caller are not passed to the scope of the callee.

This sort of isolation helps out the programmer to stay sane while dealing with data that is operated by specific sequences of instructions.

```C
void do_something() {
  // x is not available here
  int a = 33;
  int b = 55;
}

void call_something():
  int x = 100;
  do_something();
  // a and b are not available here

call_something()
```

### Global scope

There is the ability to access specific data or function declarations, if they are declared globally in relation to the scope of the procedure we are working with.

Usually it is frowned upon to alter global data from different places because it introduces confusion as to where is the data altered, and gives way for error.

```C
int x = 123;

void do_something() {
  x = x * 2;
}

void caller() {
  do_something();
  do_something();
  // at this point the value of x has been quadrupled
}
```

You can notice in the previous example that doing something like this feels tricky and introduces non-determinism.

It is however permitted and encouraged to declare global constants that functions can use, and in this way we are sure that whatever the value of the constant is, it will never change and we have a somewhat deterministic functionality. There still is however a danger if the constant is reprogrammed to a different value.

```C
const int x = 123;

int do_something(y) {
  return x * y;
}

void caller() {
  int result = do_something(5);
}
```

### Inputs and outputs

Functions can receive parameters/arguments and return a single value,
which technically represents the computation of the inputs, but it
all boils down to what the purpose of the procedure is, hence there are multiple ways of describing functions in terms of inputs and outputs:

* receives no inputs and don't return anything
* receives inputs and consumes them (doesn't return anything)
* receives no inputs and outputs something
* receives arguments and returns the result of the computation of the inputs

Or better visualised using a table:

|Inputs|Ouputs|Characteristics|
|-|-|-|
|N|N|Does **NOT** map inputs to output. Performs some hidden operations.|
|N|Y|Does **NOT** map inputs to output. Performs some hidden operations and/or retrieves something.|
|Y|N|Does **NOT** map inputs to output. Performs some hidden operations potentially based on the inputs.|
|Y|Y|Potentially maps inputs to output. Might perform some hidden operations.|

Inside the procedures, more specific examples of operations include:
* read/write from/to a file
* read/write from/to a database
* retrieve/change a global variable
* perform a system operation
* retrieve/change the state of a pixel or a set of pixels on the screen
* retrieve/change a register
* make a network request
* perform a heavy computation

#### Amount and category of arguments

The possibility of passing inputs to a procedure can be expanded even further by thinking about how many arguments and what kind of arguments are being passed.

The two main categories are:
* positional arguments - they must be passed exactly how they are expected in the procedure declared signature
* key-value association arguments - they have specific labels attached to them and they can be passed in any order desired. These also allow for default value

##### Sole positional argument

We might want to send one argument.

Example in Python:
```Python
def do_something(x: int) -> int:
  return x * 2
```

Example in C:
```C
int do_something(int x) {
  return x * 2;
}
```

##### Multiple positional arguments

Or we might want to send more arguments.

Example in Python
```Python
def do_something(a: int, b: int, c: int) -> int:
  return (a + b) * c
```

Example in C:
```C
int do_something(int a, int b, int c) {
  return (a + b) * c;
}
```

##### Indefinite positional arguments

There might be cases where we don't know how many parameters a function will be called with, so the concept of an indefinite number of arguments seems like a fitting idea.

```Python
def do_something(*args: int):
  x: int
  for (x in args):
    some_instruction

do_something(11, 22)
do_something(11, 22, 33, 44)
```

Unfortunately, C makes it difficult to express a pure call of indefinite arguments and usually, alongside a list of variable arguments, you have to pass also their count. This leads to a big problem, because it can be easy to send the wrong number of parameters being sent when calling the function, hence there is a lot of room for error.

Example in C (ellipsis):
```C
#include <stdarg.h>
void do_something(int n, ...)  // first param required by ISO C
{
  va_list args;  // declares a list of arguments
  va_start(args, n);  // copies the parameters into the args list

  int x = 0;
  for (int i = 0; i < n; i++) {
    x = va_arg(args, int); // extracts the argument and casts it
    some_instruction; // do something with x
  }
}

int main() {
  do_something(3, 11, 22, 33);
  return 0;
}
```

In the previous example (ellipsis in C), the typing is also a problem, because you don't specify what type the passed parameters have, and that can result in some type-conversion problems when
calling `va_arg`.

The same ellipsis exists in C++ as well but for the sake of a better alternative let's look at variadic templates and arguments unpacking.

Example in C++:
```C++
// T will be whatever type we want our arguments to have
// Args is just a given type name for the args, it can be anything
template <typename T, typename... Args>
void do_something(Args... args) {

  int n = sizeof...(Args);  // we get the size of all the arguments
  T arr[] = {args...};  // we unpack the parameters into an array

  // we iterate over the parameters
  for (int i = 0; i < n; i++) {
    some_instruction;  // that uses arr[i]
  }
}

int main() {
  do_something<int>(11, 22, 33);
  do_something<int>(77, 88);
  return 0;
}
```

We can start to see here some real differences amongst programming languages in terms of syntax liberalization. Some languages make it easy to express something like a variadic, while others make it dangerous or verbose.

There are other ways to send a variable number of arguments, like for example arrays or vectors. But that is a different discussion in itself.

##### Key-value association arguments

While positional arguments have their role, labeling parameters can give an advantage and clarity in code of what specific value we are passing to our procedure, ability especially useful in cases where we have a very high amount of positional arguments that make it hard to read.

Example of a ugly procedure (in Python) with many positional arguments:
```Python
def do_something(
   x: int, y: int, z: int,
   r: int, g: int, b: int,
   alpha: int,
   frame: int
):
  instruction_1
  instruction_2
  ...

do_something(10, 24, 33, 255, 0, 0, 125, 63162315)
do_something(5, 3, 2, 127, 235, 95, 67, 582915)
```

While you could argue that once you've used the function several times you will remember which number represents what, that misses the point entirely, because readability is still sacrificed for a newbie, and you could make that newbie's life easier by making it explicit. There is also the factor of fatigue, and after programming for a long time it can become difficult to follow the long list of parameters.

In Python at first hand we can just call the function `do_something` by specifically mentioning the names of the parameters:

```Python
do_something(
  x=5, y=3, z=2,
  r=127, g=235, b=95, alpha=67,
  frame=582915,
)
```

Python will know how to just redirect the values to the right arguments.

You can even combine positional arguments with keyword arguments:

```Python
do_something(
  5, 3, 2,  # still more visible than without any kwargs
  alpha=67, frame=582915,
  r=127, g=235, b=95
)
```

We could also specify default values if we'd like to:
```Python
def do_something(
   x: int = 0,
   y: int = 0,
   z: int = 0,
   r: int = 255,
   g: int = 255,
   b: int = 255,
   alpha: int = 100,
   frame: int = 0
):
  instruction_1
  instruction_2
  ...
```

You can see in the previous examples how incredibly verbose the call of the function has become.

Having default values for all arguments also means that we can call `do_something` without any parameters whatsoever.

Using keyword arguments also means that we can call the function with the parameters positions completely scrambled.

Other languages are not so allowing, and we don't actually have a direct method within C or C++ to do this. We do however have structs and classes. Let's see an example with struct.

```C
typedef struct {
  int x;
  int y;
  int z;
  int r;
  int g;
  int b;
  int alpha;
  int frame;
} DoSomethingKwargs;

void do_something(DoSomethingKwargs kwargs) {
  // we can access like kwargs.argument_name
  // instructions that use kwargs
  instruction_1;
  instruction_2;
}

int main() {
  DoSomethingKwargs kwargs = {
    .x=10, .y=25, .z=12,
    .r=255, .g=0, .b=0, .alpha=100,
    .frame=55221521
  };
  do_something(kwargs);
  return 0;
}
```

In C we are not allowed to pass the struct directly to the function, but have to store in a variable first. Alternatively in C++ you could do:

```C++
do_something({
  .x=10, .y=25, .z=12,
  .r=255, .g=0, .b=0, .alpha=100,
  .frame=55221521
});
```

#### Void, single and multiple outputs

Most functions can definitely return nothing or at least one value.

Examples in Python:
```Python
def don_not_return_anything() -> None:
  ...

def obtain_value() -> int:
  return 12
```

Examples in C:
```C
void do_not_return_anything() {
  ...
}

int obtain_value() {
  return 12;
}
```

Analogous to hardware modules, that have multiple wires going in as well as out, we should be able to return multiple values from a function as well. By default some of the languages don't support this through the syntax, and the answer is in returning lists, arrays, tuples, structs, dictionaries or hash maps.

Example in Python:
```Python
def obtain_values() -> Tuple[int, int]:
  return 11, 22

a, b = obtain_values()
```

Example in C:
```C
int * obtain_values() {
  static int results[2] = {1, 2};
  return results;
}

int * results = obtain_values();
int a = results[0];
int b = results[1];
```

Examples with named structures.

Example with dict in Python:
```Python
def obtain_dict() -> Dict[str, int]:
    return {
        'a': 11,
        'b': 22,
    }

res = obtain_dict()
a = res['a']
b = res['b']
```

Example with namedtuple in Python:
```Python
from collections import namedtuple

ResultTuple = namedtuple("ResultTuple", ['a', 'b'])

def obtain_named_tuple() -> ResultTuple:
    return ResultTuple(a=11, b=22)

res = obtain_named_tuple()
a = res.a
b = res.b
```

Example with class/dataclass in Python:
```Python
from dataclasses import dataclass

@dataclass
class Result:
    a: int
    b: int

def obtain_dataclass() -> Result:
    return Result(a=11, b=22)

res = obtain_named_tuple()
a = res.a
b = res.b
```

Example with struct in C:
```C
typedef struct {
  int a;
  int b;
} Result;


Result obtain_values() {
  Result result = {.a = 11, .b = 22};
  return result;
}

Result result = obtain_values();
int a = result.a;
int b = result.b;
```

And since there is the ability to pass an indefinite amount of input arguments, we should be able to return an indefinite amount of outputs as well.

Example in Python:
```Python
def obtain_many_values() -> Tuple[int]:
  result = list()
  ... instructions that add to the result list
  return tuple(result)

values = obtain_many_values()
```

### Reusability

The fact that you can label a sequence of instructions and call it by that label in multiple places, puts emphasis on the "do once, use multiple times" way of working.

```C
void do_something() {
  instruction_x;
  instruction_y;
  ...
}

do_something();
do_something();
do_something();
do_something();
do_something();
do_something();
... // use as many times as desired
```

### Modularity

Ability to group functions is where things get interesting in terms of possibilities, especially because modularity is tied to scoping, reusability and grouping of instructions into isolated units.

We now have the ability to unite various sequences together based on the purpose they serve together. It also allows us to create a hierarchy of dependencies that have various levels of responsibility:

* low level operations that deal with essential operations
* utility functions that reuse low level operations for specific patterns of operation
* high-level / business logic that only preoccupies itself with the essentials of functionality

## First-class functions

First-class functions are functions that can be used mostly just like that, in the sense that they can be assigned to variables and data structures, they can be passed to functions, they can be retrieved from functions etc.

The concept of first-class function starts to intersect with the domain of λ-calculus and functional programming.

As an introduction let's explore the following:

```Python
def do_something():
  ...

some_variable = do_something()
some_variable()
```

This example opens the door to a myriad of possibilities in terms of what we can do with procedures.

## Define anonymous functions

At times we might require to create a function on the fly, that can execute a sequence of instructions not needed anywhere else, its sole purpose being the need to enclose instructions in some sort of structure.

Example in Python:
```Python
anonymous_function = lambda x, y: x + y
result: int = anonymous_function(11, 22)
```

The C programming language does not have such ability but C++ does:

```C++
auto anonymous_function = [](int x, int y){return x+y;};
int result = anonymous_function(11, 22);
```

## Pass a context

Let's assume we want our procedure to get a collection of data fields and alter them based on themselves and possibly some other additional inputs.

```C
typedef struct {
  int x;
} Context;

void do_something(Context * context) {
  context->x = 11;
}
```

Which is kind of like object oriented programming, but without classes.
