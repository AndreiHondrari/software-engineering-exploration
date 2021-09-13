# Combining procedures

## Overview

Since we have a new form of organising code under labels, let us explore:
* how  the labeled procedures can be called from other procedures from within themselves
* how we can pass what procedure to be executed
by another procedure
* how we can return a procedure from a procedure

... and other more complex combinations

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

do_something(&do_this);
do_something(&do_that);
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

do_something(do_this)
do_something(do_that)
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

Or by using a fancy pointer like in C++:
```C++
#import <functional>

void do_something() {};

std::function<void()> give_function() {
  return do_something;
}

std::function<void()> some_function = give_function();
some_function();
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

### Closures: Generating a function with a function

Closures are functions created on the fly that capture some of the
enclosing scope and lives onward, even if the scope that created
the closure has ended.

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
std::function<void()> create_function() {
  return []() {
    some_instruction;
  };
}

std::function<void()> my_function = create_function();
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
#import <functional>

void do_this() {
  instruction_1;
  instruction_2;
}

void do_that() {
  instruction_x;
  instruction_y;
}

std::function<void()> wrap(
  void (*wrapee)()
) {
  return [wrapee]() {
    pre_instructions;  // pre
    wrapee();  // infix
    post_instructions;  // post
  }
}

std::function<void()> do_wrapped_this = wrap(&do_this);
do_wrapped_this();

std::function<void()> do_wrapped_that = wrap(&do_that);
do_wrapped_that();
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

#### Recursive function as a loop

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
def loop_instruction(limit: int, i: int = 0):
  if i >= limit:  # this will break the loop
    return

  some_instruction_in_direct_order
  loop_instruction(limit, i=i+1)  # recursive call
  some_instruction_in_reverse_order
```

Notice that instructions positioned before the recursive call are
executed in the order `[i...limit]` while the instructions after it are executed in reverse order `[limit...i]`.

Recursive replacement (callback):

```Python
from typing import Callable


def loop_callee(
  limit: int,
  callback: Callable[[], None],
  i: int = 0
) -> None:
  if i >= limit:  # this will break the loop
    return

  callback()
  loop_callee(limit, callback, i=i+1)


def do_this():
  instruction_1
  instruction_2


def do_that():
  instruction_x
  instruction_y


loop_callee(3, do_this)
loop_callee(2, do_that)
```

The order of the callback can be reverse as well by reversing these two lines:
```Python
loop_callee(limit, callback, i=i+1)
callback()  # now in reverse
```

#### Palindrome recursive call

If you have to execute a number of steps and then execute them in reverse right after that, you can use both the forward and the backward call.

```Python
def some_function(limit, i):
  if i >= limit:
    return

  some_instruction  # forward call
  some_function(limit, i=i+1)  # recursive call
  some_instruction  # backward call
```
