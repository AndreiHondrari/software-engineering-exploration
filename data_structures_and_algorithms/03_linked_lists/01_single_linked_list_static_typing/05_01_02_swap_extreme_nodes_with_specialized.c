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

Node * getNodeBefore(
  LinkedList * list,
  Node * referenceNode
) {
  if (
    list == NULL ||
    list->head == NULL ||
    list->head == referenceNode
  ) return NULL;

  Node * p = list->head;

  while (p != NULL && p->next != referenceNode) {
    if (p->next == referenceNode) break;
    p = p->next;
  }

  return p;
}

Node * getLastNode(LinkedList * list) {
  if (list == NULL) return NULL;

  Node * p = list->head;

  while (p != NULL && p->next != NULL) {
    p = p->next;
  }

  return p;
}

void swapExtremeNodes(LinkedList * list) {
  if (list == NULL || list->head == NULL || list->head->next == NULL) return;

  Node * first = list->head;
  Node * last = getLastNode(list);
  Node * beforeLast = getNodeBefore(list, last);

  last->next = first->next;
  first->next = NULL;
  beforeLast->next = first;
  list->head = last;
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

  printf("Before\n");
  displayList(&list);
  printf("\n");

  swapExtremeNodes(&list);

  printf("After\n");
  displayList(&list);
  printf("\n");

  clearListMemory(&list);

  return 0;
}
