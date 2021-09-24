# Design Patterns - Visitor

## Overview

Detach algorithm from the objects on which they operate.

## Use cases

- when we don't want to bloat our classes with unwanted code, we just
allow them to be visited by extension classes that will perform actions on them

## Dissection
**Element** - interface defining how nodes can accept visitors
**Visitor** - interface defining how a visitor will visit elements
**Concrete element** - implementation of elements plus specific operations of
the concrete element
**Concrete visitor** - implementation of visitor
