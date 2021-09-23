# Algorithms and data structures

## Overview

An **algorithm** is a well-defined recipe that defines the execution of a computational machine.

Purposes of an algorithm:
* calculation - obtain results
* data processing - transform data
* automatic reasoning - do this, do that

## Classification

By implementation:
* **serial** - a sequence of instructions
* **parallel / distributed** - sequences of instructions working side by side
* **recursive** - uses itself
* **logical** - provides a logical result
* **deterministic** - decisions are clear at every step
* **non-deterministic** - guesses the result; at times through heuristics; could lead to non-optimal solution
* **exact** - solution is precisely what it should be
* **approximate** - computed (most likely by guessing) until an acceptable (within desired parameters) result is obtained

By design paradigm:
* **brute-force / exhaustive** - checks every possible solution
* **divide and conquer** - reduce an instance of a problem into smaller problems until they are small enough to solve
* **decrease and conquer** - subvariant of divide and conquer where the problem set is reduced by a specific amount until an acceptable limit is hit
* **randomized** - makes choices randomly (or pseudo-randomly)
* **reduction of complexity / transform and conquer** - tranform to a better-known problem that can be solved
* **back tracking** - build multiple solutions incrementally. drop solutions that don't have acceptable characteristics
* **dynamic** - memorises solutions that have already been computed and passes them on to the next stage of execution
* **greedy** - looks for optimal solution of the substructure incrementally at each stage of the execution
* **heuristic** - alternating solution solving methods at each stage of the problem solving

By field of study:
* **search**
* **sort**
* **merge**
* **numerical**
* **graph**
* **string**
* **computational geometry**
* **combinatorial**
* **machine learning**
* **cryptography**
* **data compression**
* **parsing**

By complexity:
* **constant**
* **logarithmic**
* **linear**
* **polynomial**
* **exponential**
