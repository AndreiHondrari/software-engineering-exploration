#include <stdlib.h>
#include <stdio.h>

#include "linked_list.c"

typedef struct Queue {
  unsigned int maxSize;
  unsigned int currentSize;
  LinkedList elements;
} Queue;

typedef struct Result {
  unsigned char exists;
  int value;
} Result;

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

Result dequeue(Queue * queue) {
  Result result = {.exists = 0, .value = 0};
  if (queue == NULL || queue->currentSize == 0) return result;

  Node * node = getFirst(&(queue->elements));
  result.exists = 1;
  result.value = node->value;
  removeFirst(&(queue->elements));

  queue->currentSize -= 1;
  return result;
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

  for (int i = 0; i < SIZE + 1; ++i) {
    Result dequeueResult = dequeue(&queue);
    if (dequeueResult.exists) {
      printf("%d : Dequeue %d\n", i, dequeueResult.value);
    }
    else {
      printf("%d : No element", i);
    }
  }
  printf("\n\n");

  return 0;
}
