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

Node * insertAtStart(LinkedList * list, int newValue) {
  if (list == NULL) return NULL;

  Node * newNode = malloc(sizeof(Node));
  newNode->value = newValue;

  newNode->prev = NULL;

  if (list->head == NULL) {
    list->head = newNode;
    newNode->next = NULL;
    list->tail = newNode;
  }
  else {
    newNode->next = list->head;
    list->head = newNode;
    newNode->next->prev = newNode;
  }

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
