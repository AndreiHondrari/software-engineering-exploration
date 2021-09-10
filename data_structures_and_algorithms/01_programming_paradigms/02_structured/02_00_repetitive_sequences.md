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

## Breaking the loop

Using **break** we can immediately halt the loop and continue right after the loop body. With **continue** we skip whatever is left in the loop and proceed with the next iteration.

```C
for (int i = 0; i < 3; ++i) {
  instruction_1;
  break;
  instruction_2;
}
```

```C
for (int i = 0; i < 3; ++i) {
  instruction_1;
  continue;
  instruction_2;
}
```

## Pre and post operations

Since instructions execution is linear, introducing statements before and
after a loop can introduce certain pre-post processing capabilities as well as
it allows for parametrisation of the loop structure.

**while** variant:

```C
pre_instructions;

while (i < 3) {
  instruction_1;
  instruction_2;
  i += 1;
}

post_instructions;
```

**for** variant:

```C
pre_instructions;

for (int i = 0; i < 3; ++i) {
  instruction_1;
  instruction_2;
}

post_instructions;
```

Pre-instructions could be initialisers, range calculations, pre-filtering of the input dataset, transformation of the input dataset, etc.

Post-instructions could be post-filtering operations, post-transformation of the results, merge of the results, etc.

## Inserting or removing an instruction within the range of a loop

Depending on our needs we might decide that some instructions can sit outside or inside of a loop. We do this by altering the range.

Let's assume we have the loop
(which does an instruction 5 times: 0, 1, 2, 3, 4):
```C
for (int i = 0; i < 5; ++i) {
  some_instruction;
}
```

Extracting an instruction from the beginning would be:
```C
some_instruction;  // instruction before the loop
for (int i = 1; i < 5; ++i) // notice the lower limit (1 not 0)
{
  some_instruction;
}
```

Extracting an instruction from the end would be:
```C
for (int i = 0; i < 4; ++i) // notice the upper limit (4 not 5)
{
  some_instruction;
}
some_instruction;  // instruction after the loop
```

Extracting an instruction from the middle would be:

```C
// 0 to 4 means we will have two ranges
// 0 -> 1 for first loop
// 2 would be the middle instruction
// 3 -> 4 would be the second loop
for (int i = 0; i <= 1; ++i) // loop 0 .. 1
{
  some_instruction;
}

some_instruction;  // instruction in the middle of the range

for (int i = 3; i <= 4; ++i) // loop 3 .. 4
{
  some_instruction;
}
```

These transpositions are reversible and obviously the ranges here are small for the convenience of understanding the essentials. It wouldn't make sense to do this for small ranged loops, but rather for loops with larger ranges.

## Merging or splitting two loops

Let's assume we have the following loop:
```C
for (int i = 0; i < 100; ++i) // 0 ... 99 (100 elements)
{
  some_instruction;
}
```

Now we've already seen that loops can be split when simply trying to extract a single instruction from it, and it sometimes can result in two loops, but perhaps we don't want to extract a single instruction, and rather just split the instructions execution collection between two adjacent ranges (let's assume half as an example):

```C
for (int i = 0; i < 50)  // 0 .. 49 (50 elements, first half of 100)
{
  some_instruction;
}

for (int i = 50; i < 100)  // 50 .. 99 (50 elements, second half of 100)
{
  some_instruction;
}
```

## Note about ranges

Usually we count from 1 to n, and depending on the value of n, if we want to split the interval to a given ratio we have to consider some aspects of the limits.

Let's assume that we want to split in half, that means we want to have n/2 elements in both ranges.
If our number if even, let's say 6, we would have:
* 1, 2, 3 - for first range
* 4, 5, 6 - for second range

From which we can deduce that the ranges go:
* `1 .. n/2` - first range
* `(n/2 + 1) .. n` - second range

However in programming terms, we have the value of 0 available as well so we can shift everything one number to the left in our ranges
* 0, 1, 2 or `[0 .. (n/2 - 1)]` - first range
* 3, 4, 5 or `[n/2 .. (n - 1)]` - second range

If our number is odd we have to make a decision, as splitting an odd number, mathematically results in a real number instead of an integer, essentially meaning we are left with a remainder, which we have to decide where to place. Let's assume we have 7 elements that we need to split in two ranges.

It's either
* 0, 1, 2 - first range
* 3, 4, 5, 6 - second range

or
* 0, 1, 2, 3 - first range
* 4, 5, 6 - second range

It is really up to the programmer to determine in what way he wants to operate with the ranges and how to distribute them.

## Nested loops

Let's assume we have:

```C
int n = 2;
int m = 3;
for (int i = 0; i < n; ++i) {
  for (int j = 0; j < m; ++j) {
    some_instruction;
  }
}
```

The first question that arises is ***How many time does `some_instruction` get executed?*** to which the answer is **n multiplied by m**, hence if we have **n equivalent to m**, it only means that we will have **n<sup>2</sup>** amount of executions, or a quadratic amount.

The more the nesting goes the higher the order of the exponent goes for equal ranges. For example if we have three levels of nested loops then our amount of execution is cubic (**n<sup>3</sup>**).

## Merging non-index dependent nested loops

If you have two nested loops and you don't used the variables that are being manipulated by the loop incrementor, or if you don't have a loop incrementor like in the case of the while loop, or you don't have disjoint indexes for each of the loops, then theoretically you could reduce the loop into a flat loop that iterates in the range `0 .. n * m`.

Given:
```C
int n = 5;
int m = 6;
for (int i = 0; i < n; ++i) {
  for (int j = 0; j < m; ++j) {
    some_instruction;
  }
}
```

could become

```C
int n = 5;
int m = 6;
for (int i = 0; i < n * m; ++i) {
  some_instruction;
}
```

Of course this would be a mistake if **i** and **j** are used in the loop block for the actual instruction.

## Pre-incrementation vs post-incrementation in while loops

With **while** loops we can decide where we want the incrementation to happen:

Pre-incrementation:

```C
int x = 0;
while (x < 3) {
  x += 1; // done before the instructions sequence
  some_instruction;
}
```

which means that by the time `some_instruction` is executed, the value of x will already by 1. It also means that the counting happens from 1 to 3 in the previous example, as opposed to from 0 to 2 which occurs in post-incrementation.

Post-incrementation:

```C
int x = 0;
while (x < 3) {
  some_instruction;
  x += 1; // done after the instructions sequence
}
```

As mentioned before, range goes from 0 to 2.

## Infinite loop

If the condition that determines the halt of a loop is always true, then that loop will iterate for ever.

**while** variant:

```C
while (true) {
  some_instruction;
}
```

**for** variant:

```C
for (; true ;) {
  some_instruction;
}
```
