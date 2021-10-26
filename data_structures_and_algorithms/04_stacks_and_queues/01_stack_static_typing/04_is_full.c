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

Result pop(Stack * stack) {
  Result result = {.exists=0, .value=0};
  if (stack->currentSize == 0) return result;

  Node * first = getFirst(&(stack->elements));
  removeFirst(&(stack->elements));

  result.exists = 1;
  result.value = first->value;

  stack->currentSize -= 1;
  return result;
}

/*
0: not full
1: full
*/
unsigned char isFull(Stack * stack) {
  return stack->currentSize == stack->maxSize;
}


int main(int argc, char const *argv[]) {
  const unsigned short SIZE = 3;
  Stack stack = createStack(SIZE);

  printf("Max size: %d\n", SIZE);
  printf("Push 2 items\n");
  push(&stack, 11);
  push(&stack, 22);

  unsigned char fullStatus = isFull(&stack);
  printf("Is full? %d\n", fullStatus);

  printf("Push another one\n");
  push(&stack, 33);

  fullStatus = isFull(&stack);
  printf("Is full? %d\n", fullStatus);

  printf("Pop one\n");
  pop(&stack);

  fullStatus = isFull(&stack);
  printf("Is full? %d\n", fullStatus);

  return 0;
}
