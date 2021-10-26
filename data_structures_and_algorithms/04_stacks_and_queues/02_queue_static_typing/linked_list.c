#include <stdlib.h>

typedef struct Node {
  int value;
  struct Node * prev;
  struct Node * next;
} Node;

typedef struct LinkedList {
  struct Node * head;
  struct Node * tail;
} LinkedList;

Node * insertAtEnd(LinkedList * list, int newValue) {
  if (list == NULL) return NULL;
  Node * newNode = malloc(sizeof(Node));
  newNode->value = newValue;

  if (list->tail == NULL) {
    list->head = newNode;
    newNode->prev = NULL;
    list->tail = newNode;
  }

  else {
    newNode->prev = list->tail;
    list->tail->next = newNode;
    list->tail = newNode;
  }

  newNode->next = NULL;

  return newNode;
}

Node * getFirst(LinkedList * list) {
  if (list == NULL) return NULL;
  return list->head;
}

void removeFirst(LinkedList * list) {
  if (list == NULL || list->head == NULL) return;
  Node * p = list->head;
  list->head = list->head->next;
  if (list->head != NULL) list->head->prev = NULL;
  free(p);
}
