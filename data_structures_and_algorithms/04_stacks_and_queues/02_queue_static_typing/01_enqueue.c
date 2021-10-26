#include <stdlib.h>
#include <stdio.h>

#include "linked_list.c"

typedef struct Queue {
  unsigned int maxSize;
  unsigned int currentSize;
  LinkedList elements;
} Queue;

Queue createQueue(unsigned int maxSize) {
    Queue newQueue = {.maxSize = maxSize, .currentSize = 0};
    newQueue.elements.head = NULL;
    newQueue.elements.tail = NULL;
    return newQueue;
}

/*
0: success
1: full
2: queue pointer null
*/
unsigned char enqueue(Queue * queue, int newValue) {
  if (queue == NULL) return 2;
  if (queue->currentSize == queue->maxSize) return 1;
  insertAtEnd(&(queue->elements), newValue);
  queue->currentSize += 1;
  return 0;
}

int main(int argc, char const *argv[]) {
  const unsigned int SIZE = 3;
  Queue queue = createQueue(SIZE);

  for (int i = 1; i <= SIZE + 1; ++i) {
    int val = i * 11;
    unsigned char result = enqueue(&queue, val);
    printf("Enqueue %d : %d\n", val, result);
  }
  printf("\n");

  return 0;
}
