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
* high-level / business logic that only preocupies itself with the essentials of functionality

## Ways to combine procedures

### Subroutine

```C
// define a subroutine
void perform_instructions() {
  instruction_1;
  instruction_2;
}

void do_something() {
  // call a subroutine from a routine
  perform_instructions();
}
```

### Callback

We can pass a function to another function as an argument.

Example in C:

```C
void do_something(
  void (*some_function)()  // function pointer
) {
  some_function(); // call the callback
}

void do_this() {
  instruction_1;
  instruction_2;
}

void do_that() {
  instruction_x;
  instruction_y;
}
```

Example in Python:

```Python
def do_something(some_function):
  some_function()

def do_this():
  instruction_1
  instruction_2

def do_that():
  instruction_x
  instruction_y
```

At this point you will notice that this introduces variability in functionality, which we can further use to organise our functionalities in some interesting ways.

The ability to pass a callback procedure to another procedure means that we can surround the callback function with pre and post operations.

```Python
def do_something():
  instruction_x
  instruction_z


def do_extra_stuff(some_function):
  pre_instruction_1
  pre_instruction_2

  some_function()

  post_instruction_1
  post_instruction_2

do_extra_stuff(do_something)
```

### Returning a function

If we are able to receive a function as a function, we surely should be able to return a function as a function.

Example in C:
```C
void do_something() {
  some_instruction;
}

void (*
  give_function()  // our actual function definition
)() {
  return &do_something;
}

void (*some_function)() = give_function();

some_function();
```

Explanation on the function that returns a function definition
we have a function:

We have a function:
```C
f1() {}
```

And this function returns a pointer.

```C
*f1() {}
```

Which can be the pointer of a function:

```C
void somef() {}

void (*
  f1()
)() {
  return &somef;
};
```


Example in Python:
```Python
def do_something():
  some_instruction

def give_function():
  return do_something

some_function = give_function()
some_function()
```

### Generating a function with a function

Example in Python
```Python
def create_function():
  def new_function():
    some_instruction
  return new_function

my_function = create_function()
my_function()
```

Unfortunately C does not allow to create a function from within another function as to why nested functions are not a feature of C. **C++** however allows this through it's lambda functions:

```C++
auto create_function() {
  return [](){
    some_instruction;
  };
}

auto my_function = create_function();
my_function();
```

Because of C's limitation, we start to see the differences between programming languages and how some built-in syntax changes the way we create and think about code.

### Decorators

The ability to add pre/post operations results on subsequent calls of the same caller/callee pair for the same wrapping done in different places, and in cases like these combine with the fact that we want to change something about how the caller calls the callee, we have to correct this in that multitude of places. We start to think that maybe there is a better way, a way to memorise this signature under an alias or as a masked function, and for sure there is, given the ability to create a function inside a function.

Example in Python:
```Python
def do_this():
  instruction_1
  instruction_2

def do_that():
  instruction_x
  instruction_y

def wrap(wrapee):

  def inner():
    pre_instruction
    wrapee()
    post_instruction

  return inner

do_proxied_this = wrap(do_this)
do_proxied_that = wrap(do_that)
```

Since C does not allow for lambda functions, let's see the example in C++:
```C++

void do_this() {
  instruction_1;
  instruction_2;
}

void do_that() {
  instruction_x;
  instruction_y;
}

wrap() {
  return wrapper
}

void (*do_wrapped_this)() = wrap(&do_this);
void (*do_wrapped_that)() = wrap(&do_that);
```

### Recursion

We can call a function from within itself.

```Python
def do_something():
  do_something()
```

Now do keep in mind that doing something like in the example before will result in the function calling itself infinitely and filling up the stack, eventually hitting the upper limit and triggering an error.

Instead, you want to end the recursion at some point:

```Python
def do_something(x):
  if x > 5:
    return

  do_something(x + 1)
```

Notice in the previous example how the return instruction occurs prior to calling recursively `do_something` one more time.

There is a theory in which recursion can replace while and for loops altogether.

Classic for:
```Python
for i in [0, 1, 2, 3, 4]:
  instruction_x
```

Classic while:
```Python
while (i < 5):
  instruction_x
  i += 1
```

Recursive replacement (concrete):

```Python
def loop_instruction(i, limit):
  if i >= limit:  # this will break the loop
    return

  instruction_x
  loop_instruction(i + 1, limit)
```

Recursive replacement (callback):

```Python
def loop_callee(i, limit, callback):
  if i >= limit:  # this will break the loop
    return

  callback()
  loop_callee(i + 1, limit)


def do_this():
  instruction_1
  instruction_2


def do_that():
  instruction_x
  instruction_y


loop_callee(0, 3, do_this)
loop_callee(0, 2, do_that)
```
