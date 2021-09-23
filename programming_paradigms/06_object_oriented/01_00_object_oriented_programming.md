# Object Oriented Programming

## Base

In the beginning there was the concept of **Record** that would encompass several fields under a single label or data structure.

The C struct is a record:
```C
struct Something {
  int a;
  int b;
}
```

## TODO to cover:

* Alan Kay
  * messaging
  * local retention, protection and hiding of state-process
  * late binding
* contravariance and covariance
* invariants
* implementation inheritance
* subtyping
* category theory
* composition
* data abstraction (specification vs implementation)
* Barbara Liskov
* David Parnas - criteria of modular decomposition
* shared state vs local state
* encapsulation
* information hiding
* DCI - Data, Context and Interaction -> objects are representations of data that take different roles in specific contexts
* Trygve Reenskaug - OOram method
* Behavioral subtyping
* Liskov Substitution Principle
* Bertrand Meyer
* SOLID
  * Single-Responsibility Principle
  * Open/closed principle
  * Liskov Substitution Principle
  * Interface segregation principle
  * Dependency Inversion Principle
* single-inheritance vs multi-inheritance
* diamond resolve for multi-inheritance
* interfaces
* abstract classes / virtual classes
* class based vs prototype based
* meta classes
* overridding
* Domain-Driven Design
* Tony Hoare - correctness of the program
* polymorphism
  * ad-hoc polymorphism - different functions with similar name that act with different implementations for different types of inputs - overloading
  * parametric polymorphism - write a generic function or class that allows you to specify the type to be used at a later time - C++ templates, Python generics - assumes an exact specification of the type that is passed, meaning the type of operations that can be performed on it
  * subtype polymorphism - subclasses that have the same operations like the superclass can be passed to a function that expects an object of the superclass type - LSP principle - alternates implementation
