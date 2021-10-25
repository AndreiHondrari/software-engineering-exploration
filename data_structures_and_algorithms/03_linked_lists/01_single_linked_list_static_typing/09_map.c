#include <stdio.h>
#include <stdlib.h>


typedef struct Node {
  int value;
  struct Node * next;
} Node;


typedef struct LinkedList {
  Node * head;
} LinkedList;


void insertInListAtEnd(LinkedList * list, int newValue) {
  if (list == NULL) return;

  // create new node
  Node * newNode = malloc(sizeof(Node));
  newNode->value = newValue;
  newNode->next = NULL;

  // handle empty list
  if (list->head == NULL) {
    list->head = newNode;
  }

  // append new node
  else {
    // get to the last node
    Node * p = list->head;
    while (p->next != NULL) {
      p = p->next;
    }

    // attach it to the last node
    p->next = newNode;
  }
}

void displayList(LinkedList * list) {
  if (list == NULL) return;

  Node * p = list->head;
  while (p != NULL) {
    printf("%p { %d } -> %p \n", p, p->value, p->next);
    p = p->next;
  }
}

void mapList(LinkedList * list, int (*transformFunc)()) {
  if (list == NULL || transformFunc == NULL) return;
  Node * p = list->head;
  while (p != NULL) {
    p->value = transformFunc(p->value);
    p = p->next;
  }
}

void clearListMemory(LinkedList * list) {
  Node * p = list->head;
  Node * pNext;
  while (p != NULL) {
    pNext = p->next;
    free(p);
    p = pNext;
  }

  list->head = NULL;
}

int transformValue(int n) {
  int val = (n * 10 + n);
  return val * val;
}

int main(int argc, char const *argv[]) {

  LinkedList list = {.head=NULL};

  insertInListAtEnd(&list, 1);
  insertInListAtEnd(&list, 2);
  insertInListAtEnd(&list, 3);
  insertInListAtEnd(&list, 4);
  insertInListAtEnd(&list, 5);

  printf("Before\n");
  displayList(&list);
  printf("\n");

  mapList(&list, &transformValue);

  printf("After\n");
  displayList(&list);
  printf("\n");

  clearListMemory(&list);

  return 0;
}
