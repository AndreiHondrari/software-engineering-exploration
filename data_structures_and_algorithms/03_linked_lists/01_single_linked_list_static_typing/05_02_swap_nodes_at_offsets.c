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

void swapNodes(
  LinkedList * list,
  unsigned char offset_1,
  unsigned char offset_2
) {
  if (
    list == NULL ||
    list->head == NULL ||
    list->head->next == NULL ||
    offset_1 == offset_2
  ) return;

  Node * beforeFirst = NULL;
  Node * first = NULL;

  Node * beforeSecond = NULL;
  Node * second = NULL;

  Node * p = list->head;
  Node * q = NULL;

  int i = 0;
  while (p->next != NULL) {

    if (i == offset_1) {
      beforeFirst = q;
      first = p;
    }

    if (i == offset_2) {
      beforeSecond = q;
      second = p;
    }
    
    q = p;
    p = p->next;

    ++i;
  }

  if (first != NULL && second != NULL) {
    beforeFirst->next = second;
    beforeSecond->next = first;
    Node * temp = first->next;
    first->next = second->next;
    second->next = temp;
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

  printf("Before\n");
  displayList(&list);
  printf("\n");

  swapNodes(&list, 1, 5);

  printf("After\n");
  displayList(&list);
  printf("\n");

  clearListMemory(&list);

  return 0;
}
