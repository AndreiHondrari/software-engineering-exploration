# Imperative paradigm

## Overview

The imperative paradigm is probably the fundamental way of writing code, by simply making statements of what the program should do in simple and clear operations: assign this variable, evaluate this mathematical expression, delete this piece of memory, etc.

## Components

The most basic part of software code is the instruction, which is usually one line, one expression, one call to do something.

Examples:
* assign a variable
* perform an arithmetic operation
* evaluate a logic (boolean) expression
* allocate/deallocate a space of memory
* read from an input
* write to an output

Instructions can be grouped in sequences that execute one after another in
orderly fashion.


## Static behaviour vs parametrised

In the simples of ways, a statement will do something completely fixed, static or obvious like calculating a number from two other numbers, or printing a piece of text on the screen. This behaviour will output different results only by altering the piece of code to introduce new information that will lead to providing us with the new desired results. This form of data introduction is tedious at most and we would like our software to perform the same functionality
on variable inputs of data. This is where variable assignment is extremely important and allows us to alter the execution and outcome of our statements.

Let's assume the following:

```C
int x = 11;

y = x * 2 + 100;  // some mathematical formula
```

This is the most basic form of using a variable value within a statement. In the previous example however we assigned the value of x within the program, but this value could easily come from a file, from the keyboard or from the network, allowing us to alter dynamically the execution and outcome of our sequence of instructions. The process of introducing variable data and behaviour is called parametrisation.

Of course this example can get more complicated by introducing more variables.

The thing with parametrisation is that one man's trash is another man's treasure, meaning that the output of one sequence can become the input for another sequence, hence we have the ability to chain sequences either in the same program or the execution process itself.

Let's assume that we have two programs with different sequences where both of them read and write to the same file, overwriting the value they find within the file. If we were to execute the two programs in one sequence or the reverse sequence, our outcome would be totally different based on this variability of execution chain.

At this point you might notice that this kind of arrangement looks a lot like modules and modularisation, allowing one to configure and reconfigure a sequence of statements (aka a block) in a variety of ways, giving way for emerging structures.

## Sequence matters

Let's assume the two following examples:

Sequence 1:
```C
int x = 2;
x = x * 2;
int z = x + 10;
```

Sequence 2:
```C
int x = 2;
int z = x + 10; // flipped
x = x * 2;  // flipped
```

Notice how in sequence 2, the `x = x * 2` happens after `int z = x + 10`. Now the two sequences have different outcome for z. In sequence 1 z will be 14, when in sequence 2 it will be 12. The way the instructions roll in a sequence is of extreme importance.
