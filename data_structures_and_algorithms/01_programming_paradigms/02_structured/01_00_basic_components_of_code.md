# Basic components of code

## Overview

Structural paradigm offers us the ability to position sequences of instructions under control structures that
select one sequence or another for execution, or simply repeats a given sequence a number of times.
This type of programming leverages the jump operation at the microarchitecture level.

## Control flow

### The IF

The most basic way to control if a sequence of instructions is to be executed or not is via the IF conditional statement/expression, which will execute the sequence when the condition attached to it is true.

```C
if (logic_expression) {
  instruction_1;
  instruction_2;
}
```

### The IF-ELSE

Sometimes we just want to execute a different sequence of instructions for the complementary value of the logical expression.
At this point the code starts to branch in two execution flows.

```C
if (logic_expression) {
  instruction_1;
  instruction_2;
}

else {
  // or do the fallback sequence of instructions instead
  fallback_instruction_1;
  fallback_instruction_2;
}
```

### The IF-ELSE-IF

Sometimes we want to check for multiple logical expressions that are checked subsequently when the previous one failed.
This allows the branching of the execution flow in multiple directions.

```C
if (logic_expression) {
  // first sequence
  instruction_1;
  instruction_2;
}

else if (logic_expression_2) {
  // second, alternative sequence
  alternative_instruction_1;
  alternative_instruction_2;
  alternative_instruction_3;
}

else if (logic_expression_3) {
  // third, alternative sequence
  alternative_instruction_4;
  alternative_instruction_5;
  alternative_instruction_6;
}
```

### The IF-ELSE-IF-ELSE

And ultimately, we want to be able to combine multiple conditional branches with a fallback.

```C
if (logic_expression) {
  instruction_1;
  instruction_2;
}

else if (logic_expression_2) {
  // alternative sequence
  alternative_instruction_1;
  alternative_instruction_2;
  alternative_instruction_3;
}

else {
  // or do the fallback sequence of instructions instead
  fallback_instruction_1;
  fallback_instruction_2;
}
```

### Nested conditioned sequences

The ability to use an IF-conditioned sequence of instructions as a sequence itself, opens the door to countless execution flow branching possibilities.

```C
if (level_1_logic_expression) {
  if (level_2_logic_expression) {
    instruction_1;
  }
}
```

### Inverting the order of the IF-ELSE blocks by negating the condition

If we have a plain old IF-ELSE conditional structure

```C
if (expression) {
  instruction_1;
}
else {
  instruction_2;
}
```

we can simply invert the blocks by negating the expression as such:

```C
if (!expression) {  // notice the NOT operator
  instruction_2; // notice the different instruction
}
else {
  instruction_1; // notice the different instruction
}
```


### Reducing conditioned sequence

It might be desirable at times to reduce such constructs to simpler alternatives. To exemplify this, let us define the following logic operations:
* AND noted as **&&**
* OR noted as **||**
* NOT noted as **!**
* XOR noted as **^**

Examples (where **a** and **b** are boolean values: **true**/**false**):
* `a && b`
* `a || b`
* `!a`
* `a ^ b`

### Reduce two IF-conditioned sequences with similar condition

Let's assume we have the two following sequences:

```C

if (some_expression) {
  instruction_1;
}

if (some_expression) {
  instruction_2;
}
```

in this case we could group both sequences under the same IF block:

```C
if (some_expression) {
  instruction_1;
  instruction_2;
}
```

### Reduce a nested IF-conditioned sequences
To reduce a positive branch nested if, we simply chain the expressions together under a single if.

```C
if (level_1_logic_expression && level_2_logic_expression) {
  instruction_1;
}
```

There might be ELSE's involved, and in that case we must be careful not to break the actual execution flow.

```C
if (expression_1){
  if (expression_2) {
    instruction_1;
  }
  else {
    instruction_2;
  }
}
```

and if we try to do:

```C
// BAD

if (expression_1 && expression_2) {
  instruction_1;
}

else {
  instruction_2;
}
```

it will execute `instruction_2` for those cases where `expression_1` is false, which was not the case when the IF-conditioned sequences were nested, therefore breaking the original execution flow. We can do something like this only if the first IF-conditioned sequence also has an ELSE-conditioned sequence identical to the one that is nested.

An actual equivalent alternative would be:

```C
if (expression_1 && expression_2)
{
  instruction_1;
}

if (expression_1 && !expression_2)  // notice the negation of expression_2
{
  instruction_2;
}
```


### Transposing IF-conditioned sequences with pre/post sequences

We might have nested IF-conditioned sequences that are not entirely similar.

```C
if (expression_1) {
  instruction_x;  // pre instruction

  if (expression_2) {
    instruction_1;
  }

  instruction_z;  // post instruction
}
```

for which we might want to split the sequence to accommodate a more flat code.

```C
if (expression_1) {
  instruction_x;
}

if (expression_1 && expression_2) {
  instruction_1
}

if (expression_1) {
  instruction_z;
}
```

notice the additional IF-conditioned sequence. The execution of `instruction_x`, `instruction_1` and `instruction_z` is the same, and the condition of their execution is the same. The only thing that changed is the form.

We could also have pseudo-similar neighbouring IF-conditioned sequences:

```C
if (expression_1) {
  instruction_1;
}

if (expression_2) {
  instruction_1;
  instruction_2;
}
```

which can be transformed to:

```C
if (expression_1 || expression_2) {
  instruction_1;
}

if (expression_2) {
  instruction_2;
}
```

### Reducing nested IF-conditioned sequences according to XOR

At times we can transform code that has nested IF blocks whose conditions satisfy the XOR table truth (true only when a subset of the inputs are true and not all of them).

```C
if (expression_1) {
  if (!expression_2) {
    instruction_1;
    instruction_2;
  }
}

else {  // equivalent to if (!expresion_1)
  if (expression_2) {
    instruction_1;
    instruction_2;
  }
}
```

reducing to:

```C

if (expression_1 ^ expression_2) {
    instruction_1;
    instruction_2;
}

```
