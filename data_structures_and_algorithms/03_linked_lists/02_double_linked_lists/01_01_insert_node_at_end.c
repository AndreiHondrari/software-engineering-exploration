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

  insertNodeAtEnd(&list, 11);
  insertNodeAtEnd(&list, 22);
  insertNodeAtEnd(&list, 33);

  printf("FORWARD\n");
  displayList(&list);

  printf("BACKWARD\n");
  displayListBackward(&list);

  clearListMemory(&list);

  return 0;
}
