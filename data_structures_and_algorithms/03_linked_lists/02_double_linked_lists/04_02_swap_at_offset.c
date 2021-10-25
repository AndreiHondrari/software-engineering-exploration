#include <stdlib.h>
#include <stdio.h>

typedef struct Node {
  int value;
  struct Node * prev;
  struct Node * next;
} Node;

typedef struct LinkedList {
  struct Node * head;
  struct Node * tail;
} LinkedList;

Node * insertNodeAtEnd(LinkedList * list, int newValue) {
  if (list == NULL) return NULL;

  Node * newNode = malloc(sizeof(Node));
  newNode->value = newValue;

  if (list->tail == NULL) {
    newNode->prev = NULL;
    newNode->next = NULL;
    list->head = newNode;
  } else {
    list->tail->next = newNode;
    newNode->prev = list->tail;
  }

  list->tail = newNode;

  return newNode;
}

void swapAt(
  LinkedList * list,
  unsigned int offset_1,
  unsigned int offset_2
) {
  if (list == NULL || list->head == NULL || offset_1 == offset_2) return;

  const unsigned int BIGGEST_OFFSET = (
    (offset_1 > offset_2) ? offset_1 : offset_2
  );

  Node * first = NULL;
  Node * second = NULL;

  Node * p = list->head;

  int i = 0;
  while (p != NULL && i <= BIGGEST_OFFSET) {
    if (i == offset_1) first = p;
    if (i == offset_2) second = p;
    p = p->next;
    ++i;
  }

  if ( (first != NULL) && (second != NULL)) {
    Node * beforeFirst = first->prev;
    Node * beforeSecond = second->prev;
    Node * afterFirst = first->next;
    Node * afterSecond = second->next;

    // rewire nexts for prevs
    if (beforeFirst != NULL) beforeFirst->next = second;
    if (beforeSecond != NULL) beforeSecond->next = first;

    // rewire prevs for nexts
    if (afterFirst != NULL) afterFirst->prev = second;
    if (afterSecond != NULL) afterSecond->prev = first;

    // rewire prevs for nodes
    first->prev = beforeSecond;
    second->prev = beforeFirst;

    // rewire nexts for nodes
    first->next = afterSecond;
    second->next = afterFirst;

    // rewire head and tail

    if (offset_1 < offset_2) {
      if (beforeFirst == NULL) {
        list->head = second;
      }

      if (afterSecond == NULL) {
        list->tail = first;
      }
    }

    // or if bigger
    else {
      if (afterFirst == NULL) {
        list->tail = second;
      }

      if (beforeSecond == NULL) {
        list->head = first;
      }
    }
  }
}

void displayList(LinkedList * list) {
  if (list == NULL || list->head == NULL) return;
  Node * p = list->head;
  while (p != NULL) {
    printf("%p { %d }\n", p, p->value);
    p = p->next;
  }
  printf("\n");
}

void displayListBackward(LinkedList * list) {
  if (list == NULL || list->head == NULL) return;
  Node * p = list->tail;
  while (p != NULL) {
    printf("%p { %d }\n", p, p->value);
    p = p->prev;
  }
  printf("\n");
}

void clearListMemory(LinkedList * list) {
  if (list == NULL || list->head == NULL) return;

  Node * p = list->head;
  Node * pNext = p->next;
  while (p != NULL) {
    pNext = p->next;
    free(p);
    p = pNext;
  }
}

int main(int argc, char const *argv[]) {
  LinkedList list = {.head = NULL};

  int values[] = {11, 22, 33, 44, 55};
  const unsigned int SIZE = sizeof(values) / sizeof(int);

  for (int i = 0; i < SIZE; ++i) {
    insertNodeAtEnd(&list, values[i]);
  }

  printf("ORIGINAL\n");
  displayList(&list);

  swapAt(&list, 1, 3);

  printf("FORWARD\n");
  displayList(&list);

  printf("BACKWARD\n");
  displayListBackward(&list);

  clearListMemory(&list);

  return 0;
}
