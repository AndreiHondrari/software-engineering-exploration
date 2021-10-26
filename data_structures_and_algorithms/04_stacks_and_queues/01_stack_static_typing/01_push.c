#include <stdlib.h>
#include <stdio.h>

#include "linked_list.c"

typedef struct Stack {
  unsigned int maxSize;
  unsigned int currentSize;
  LinkedList elements;
} Stack;


Stack createStack(unsigned int maxSize) {
  Stack newStack = {.maxSize = maxSize, .currentSize = 0};
  newStack.elements.head = NULL;
  newStack.elements.tail = NULL;
  return newStack;
}

/*
0: success
1: full
2: stack pointer null
*/
unsigned char push(Stack * stack, int value) {
  if (stack == NULL) return 2;
  if (stack->currentSize == stack->maxSize) return 1;
  insertAtStart(&(stack->elements), value);
  stack->currentSize += 1;
  return 0;
}


int main(int argc, char const *argv[]) {
  Stack stack = createStack(5);

  for (int i = 1; i <= 6; ++i) {
    int val = i * 11;
    unsigned char result = push(&stack, val);
    printf("Push %d: %d\n", val, result);
  }

  return 0;
}
