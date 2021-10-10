# Data structures and algorithms objectives

## Overview

We have all these data representations and recipes to analyse or alter these
representations, but what are the potential uses of them?

## Objectives

### Data structures objectives

#### Bit

|purpose|possibilities|
|-|-|
|evaluate|is set, is null, is correct, and, or, xor, nor, nand, nxor|
|iterate|-|
|match|against 1 or 0|
|count|-|
|search|-|
|change|force to 0, force to 1|
|sort|-|
|swap|intermediary variable swap, xor swap|
|invert|complement, negation, bit flip, xor 0b1 flip|
|reverse|-|
|generate/create|= 1, = 2|
|copy|yes|
|remove|-|
|compute|add (creates carry bit)|
|concatenate|results in a bitfield of two|
|merge|and, or, xor, nor, nand, nxor|
|decompose|-|
|extract|bit mask|
|convert|decoder, inversion|
|decide|branching and loop conditions are binary|
|dispatch|based on 0=false and 1=true, mux, demux|
|learn|memorise effects of 0 and 1|
|control|similar to decision|
|gather|a bit - not much to gather|
|analyse|-|

#### Bitfields

|purpose|possibilities|
|-|-|
|evaluate|is null 0x00, is not null 0x00, and, or, xor, nor, nand, nxor, specific bit, specific group of bits, detect power of two|
|iterate|bit by bit or groups of bits, by shifting|
|match|equals to bitfield, AND with 0xFF is different from 0x00, flags|
|count|count bits of 1, count bits of 0, count groups of bit formations (00, 01, 10, 11, 001, 010, etc.)|
|search|for 0 in field of 1s, for 1 in field of 0s, for bit formations|
|change|left most bit, right most bit, n-th bit, group of bits, all bits, pull up, pull down, according to evaluation|
|sort|0s to the left and 1s to the right and viceversa, formations of bits by criteria (value, specific bit/bit group set or not set)|
|swap|left most with rightmost bit, group of bits, n-th bit with m-th bit|
|invert|left most bit, right most bit, nthbit, group of bits, all bits, xor operation with mask|
|reverse|yes|
|generate/create|patterns of alternating bits or groups of alternating bits, increasing amount of 1s separated by a 0 and 0s separated by 1, fill 1s from lsb/msb, fill 1s from position|
|copy|OR operation of bitfield with 0x00 and store into new variable, AND operation of bitfield with mask and store into new variable|
|remove|pull down or pull up depending on which type of logic is used (negative or positive)|
|compute|addition, subtraction|
|concatenate|results in larger bitfields|
|merge|two bitfields, bits of a bitfield amongst themselves into a final bit, selective masking, and, or, overlap part of head with part of tail (a kind of overlapping concatenation)|
|decompose|extract groups of bits into parts (like left nibble and right nibble of a byte)|
|extract|right most bit, left most bit, nth bit, bit mask of specific bits, bit mask of null, bit mask of full|
|convert|shift (left or right), encrypt/decrypt|
|decide|based on a bit, based on a part of the bitfield, based on evaluation and matching operations|
|dispatch|based on evaluation and matching operations|
|learn|memorise patterns of bitfields|
|control|flag based, decision and matching based|
|gather|bit by bit, group of bits by group of bits, with and without offset|
|analyse|ratio of bits, ratio of groups of bits, how many bits '**a**' are followed by bits '**b**', most frequent bitfields, amount of bitfields that have the n-th bit either 0 or 1|

#### Integers

|purpose|possibilities|
|-|-|
|evaluate|(non)equality, odd/even|
|iterate|digit by digit, group of digits by group of digits|
|match|complete number, part of the number|
|count|a specific digit, a group of digits, amount of digits in the number, amount of values that have a specific n-th digit|
|search|a digit, a group of digits|
|change|a digit, a group of digits, add a digit to a specific digit (with carry), set digit to 0, set digit to specific value|
|sort|digits, group of digits by criteria (by value)|
|swap|n-th with m-th digit, groups of digits|
|invert|complement, negative|
|reverse|all digits, groups of digits|
|generate/create|patterns of digits|
|copy|a digit/group of digits from a position to another, a whole number into another variable, a digit/group of digits to another number|
|remove|a digit, a group of digits|
|compute|arithmetic operations|
|concatenate|into a larger number, overlapping|
|merge|numbers into a value by operation, addition, subtraction, multiplication, division, digits into a final value by operation|
|decompose|into digits, into groups of digits|
|extract|n-th digit (units, tens, hundreds, thousands), groups of digits, digit that matches a criteria (filtering)|
|convert|offset value with a constant, n-plicate a value, disregard sign|
|decide|based on value, based on part of the value|
|dispatch|to a numbered branch based, based on the evaluation and matching|
|learn|patterns of digits in a number, average value, most frequent value|
|control|value based, decision and matching based|
|gather|digit by digit, group of digits by group of digits, with and without offset|
|analyse|ratio of specific digits, average value|

#### Arrays

|purpose|possibilities|
|-|-|
|evaluate|(mapping) depends on the type of the element|
|iterate|one/multiple element at a time|
|match|against a reference array (partly or completely)|
|count|amount of elements, elements of a specific value, how many elements '**a**' are followed by an element '**b**', amount of arrays that have n-th element of a specific value|
|search|specific element or multiple elements (in specific sequence)|
|change|one element, n elements|
|sort|based on value, based on part of the value|
|swap|any two elements|
|invert|(mapping) depends on the type of the element|
|reverse|all elements or groups of elements|
|generate/create|element patterns - depends on the type of the elements|
|copy|an element/a group of elements from one side to another or to a different array|
|remove|depends on the programming language|
|compute|reduce/accumulate all/k the elements into a single value according to the value type, combinations|
|concatenate|two arrays into a larger array|
|merge|corresponding values of elements from two arrays according to the type of the value type, zipping elements into a new array according to a pattern (one from this and one from that, two from this and one from that)|
|decompose|into single elements, specific sub-arrays of given length, sub-arrays of distinct values|
|extract|elements that match a criteria (filtering), every n-th element, consecutive elements that match a criteria|
|convert|map the values to a function to alter them according to an operation, produce an array that represents a computation of the original according to some rules|
|decide|based on the size of the array, based on a specific element or a group of elements of the array|
|dispatch|for each element do something specific depending on its value or part of the value|
|learn|remember most frequent or all elements used in an array, remember the positions some numbers take most often or ever|
|control||
|gather|one element at a time, group of elements at a time|
|analyse|ratio of specific elements in the array|

#### Multi-dimensional Arrays

|purpose|possibilities|
|-|-|
|evaluate||
|iterate||
|match||
|count||
|search||
|change||
|sort||
|swap||
|invert||
|reverse||
|generate/create||
|copy||
|remove||
|compute||
|concatenate||
|merge||
|decompose||
|extract||
|convert||
|decide||
|dispatch||
|learn||
|control||
|gather||
|analyse||

#### Linked lists

|purpose|possibilities|
|-|-|
|evaluate||
|iterate||
|match||
|count||
|search||
|change||
|sort||
|swap||
|invert||
|reverse||
|generate/create||
|copy||
|remove||
|compute||
|concatenate||
|merge||
|decompose||
|extract||
|convert||
|decide||
|dispatch||
|learn||
|control||
|gather||
|analyse||

#### XX

|purpose|possibilities|
|-|-|
|evaluate||
|iterate||
|match||
|count||
|search||
|change||
|sort||
|swap||
|invert||
|reverse||
|generate/create||
|copy||
|remove||
|compute||
|concatenate||
|merge||
|decompose||
|extract||
|convert||
|decide||
|dispatch||
|learn||
|control||
|gather||
|analyse||

#### XX

|purpose|possibilities|
|-|-|
|evaluate||
|iterate||
|match||
|count||
|search||
|change||
|sort||
|swap||
|invert||
|reverse||
|generate/create||
|copy||
|remove||
|compute||
|concatenate||
|merge||
|decompose||
|extract||
|convert||
|decide||
|dispatch||
|learn||
|control||
|gather||
|analyse||

#### XX

|purpose|possibilities|
|-|-|
|evaluate||
|iterate||
|match||
|count||
|search||
|change||
|sort||
|swap||
|invert||
|reverse||
|generate/create||
|copy||
|remove||
|compute||
|concatenate||
|merge||
|decompose||
|extract||
|convert||
|decide||
|dispatch||
|learn||
|control||
|gather||
|analyse||

#### XX

|purpose|possibilities|
|-|-|
|evaluate||
|iterate||
|match||
|count||
|search||
|change||
|sort||
|swap||
|invert||
|reverse||
|generate/create||
|copy||
|remove||
|compute||
|concatenate||
|merge||
|decompose||
|extract||
|convert||
|decide||
|dispatch||
|learn||
|control||
|gather||
|analyse||
