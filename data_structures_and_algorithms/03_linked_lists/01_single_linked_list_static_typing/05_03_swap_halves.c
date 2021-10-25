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

Node * getLastNode(LinkedList * list) {
  if (list == NULL) return NULL;

  Node * p = list->head;

  while (p != NULL && p->next != NULL) {
    p = p->next;
  }

  return p;
}


Node * getNodeAt(LinkedList * list, unsigned int offset) {
  if (list == NULL) return NULL;

  Node * p = list->head;

  int i = 0;
  while (p != NULL && i < offset) {
    p = p->next;
    ++i;
  }

  return p;
}

unsigned int getListSize(LinkedList * list) {
  unsigned int result = 0;

  Node * p = list->head;
  while (p != NULL) {
    result += 1;
    p = p->next;
  }

  return result;
}

void swapHalves(LinkedList * list) {
  if (
    list == NULL ||
    list->head == NULL ||
    list->head->next == NULL
  ) return;

  unsigned int size = getListSize(list);
  unsigned int middleIndex = (int) (size / 2);

  // obtain nodes of interest
  Node * first = list->head;
  Node * beforeMiddle = getNodeAt(list, middleIndex - 1);
  Node * middle = getNodeAt(list, middleIndex);
  Node * last = getLastNode(list);

  // perform swap
  list->head = middle;
  last->next = first;
  beforeMiddle->next = NULL;
}

void displayList(LinkedList * list) {
  if (list == NULL) return;

  Node * p = list->head;
  while (p != NULL) {
    printf("%p { %d } -> %p \n", p, p->value, p->next);
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

int main(int argc, char const *argv[]) {

  LinkedList list = {.head=NULL};

  insertInListAtEnd(&list, 111);
  insertInListAtEnd(&list, 222);
  insertInListAtEnd(&list, 333);
  insertInListAtEnd(&list, 444);
  insertInListAtEnd(&list, 555);
  insertInListAtEnd(&list, 666);
  insertInListAtEnd(&list, 777);
  insertInListAtEnd(&list, 888);

  printf("Before\n");
  displayList(&list);
  printf("\n");

  swapHalves(&list);

  printf("After\n");
  displayList(&list);
  printf("\n");

  clearListMemory(&list);

  return 0;
}
