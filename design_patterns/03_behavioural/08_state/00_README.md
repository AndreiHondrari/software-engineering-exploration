# Design Patterns - State

## Overview

Instance changes behaviour based on its state.

## Use cases

- TCP connection behaves differently based on its connectivity state
- NPC (Non-player character) in game changes aggression behaviour based on
its state in relation to you the human player

## Dissection

**State** - interface defining what concrete states operations should be
**Concrete state** - implements the state functionality
**Context** - holds the current state and delegates function calls to the state
instance
