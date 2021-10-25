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

Node * getNodeAtOffset(LinkedList * list, unsigned int offset) {
  if (list == NULL) return NULL;

  Node * p = list->head;
  int i = 0;
  while (p != NULL && i < offset) {
    p = p->next;
    ++i;
  }

  return p;
}

void removeAt(LinkedList * list, unsigned int offset) {
  if (list == NULL || list->head == NULL) return;

  Node * p = getNodeAtOffset(list, offset);
  p->prev->next = p->next;
  p->next->prev = p->prev;
  free(p);
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

  removeAt(&list, 3);

  printf("FORWARD\n");
  displayList(&list);

  printf("BACKWARD\n");
  displayListBackward(&list);

  clearListMemory(&list);

  return 0;
}
