#include <stdlib.h>
#include <stdio.h>

#include "linked_list.c"

typedef struct Stack {
  unsigned int maxSize;
  unsigned int currentSize;
  LinkedList elements;
} Stack;

typedef struct Result {
  unsigned char exists;
  int value;
} Result;


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

Result getTop(Stack * stack) {
  Result result = {.exists=0, .value=0};
  if (stack == NULL || stack->currentSize == 0) return result;

  Node * first = getFirst(&(stack->elements));
  result.exists = 1;
  result.value = first->value;

  return result;
}


int main(int argc, char const *argv[]) {
  const unsigned short SIZE = 3;
  Stack stack = createStack(SIZE);

  for (int i = 1; i <= SIZE; ++i) {
    int val = i * 11;
    unsigned char result = push(&stack, val);
    printf("Push %d: %d\n", val, result);
  }
  printf("\n");

  Result result = getTop(&stack);
  printf("Top: %d\n", result.value);

  result = getTop(&stack);
  printf("Top: %d\n", result.value);

  return 0;
}
