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

/*
0: success
1: fail
*/
unsigned char insertInListAtOffset(
  LinkedList * list,
  unsigned int offset,
  int newValue
) {
  if (list == NULL) return 1;

  // create new node
  Node * newNode = malloc(sizeof(Node));
  newNode->value = newValue;

  // get at offset
  int i = 0;
  Node * p = list->head;
  Node * q = NULL;

  while (p != NULL && i < offset) {
    q = p;
    p = p->next;
    ++i;
  }

  if (p == NULL) return 1;

  Node * oldNodeAtOffset = p;
  q->next = newNode;
  newNode->next = oldNodeAtOffset;
  oldNodeAtOffset->next = p->next;

  return 0;
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

  for (int i = 1; i < 5; ++i) {
    int val = 10 * i + i;
    insertInListAtEnd(&list, val);
  }

  printf("Before\n");
  displayList(&list);
  printf("\n");

  insertInListAtOffset(&list, 2, 777);

  printf("After\n");
  displayList(&list);
  printf("\n");

  clearListMemory(&list);

  return 0;
}
