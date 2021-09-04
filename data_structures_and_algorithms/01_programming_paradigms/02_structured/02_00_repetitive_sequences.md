# Repetitive sequences of instruction

## Overview

Let's assume we have the following piece of code:

```C
instruction_1;
instruction_2;
instruction_1;
instruction_2;
instruction_1;
instruction_2;
```

we notice that the sequence repeats a couple of instructions in the same
sequence, a number of times (in this case 3). What if we were to rewrite
this as a more compressed form, depicting the fact that it repeats in a loop
for 3 times? Wouldn't that make things easier? But of course.

## The while loop

Simply iterates as long as its condition is true.

```C
int i = 0;
while (i < 3) {
  instruction_1;
  instruction_2;
  i += 1;
}
```

## The do/while loop

Same like while but executes first and only after that checks the condition.

```C

do {
  instruction_1;
  instruction_2;
  i += 1;
} while (i < 3)
```

## While vs do-while

The classic argument of using a do-while over a while loop is that you can use it when you want to execute a sequence of instructions at least once before hitting the condition, but this is not a strong argument against using only the while, hence why some languages have only the while loop and not the do-while.

## The for loop

Depending on the language the for loop will either use the three-component system or will simply iterate over a collection of items:

In C:

```C
// three components
// (initializer; condition; incrementor)
for (int i = 1; i <= 5; ++i) {
  instruction_1;
  instruction_2;
}
```

In Python:

```Python
for x in [1, 2, 3, 4, 5]:
  instruction_1
  instruction_2
```
