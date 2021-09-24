# Design Patterns - Template method

## Overview

Define some operations that use other undefined operations, which are
implemented by subclasses

## Use cases
- when you have to use some operations, but you don't know how those operations
will be implemented
- when you want to allow subclass implementors define how to do primitive
operations

## Dissection
- **Abstract** - supertype defining some operation that uses other
unimplemented primitive operations
- **Subclass** - subtype of abstract that implements the primitive operations
