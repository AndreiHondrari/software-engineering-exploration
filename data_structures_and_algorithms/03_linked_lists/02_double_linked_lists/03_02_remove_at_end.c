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

void removeEndNode(LinkedList * list) {
  if (list == NULL || list->head == NULL) return;

  Node * p = list->tail;
  list->tail = list->tail->prev;
  list->tail->next = NULL;
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

  int values[] = {11, 22, 33};
  const unsigned int SIZE = sizeof(values) / sizeof(int);

  for (int i = 0; i < SIZE; ++i) {
    insertNodeAtEnd(&list, values[i]);
  }

  printf("ORIGINAL\n");
  displayList(&list);

  removeEndNode(&list);

  printf("FORWARD\n");
  displayList(&list);

  printf("BACKWARD\n");
  displayListBackward(&list);

  clearListMemory(&list);

  return 0;
}
