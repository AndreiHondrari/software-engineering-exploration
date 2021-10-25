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

LinkedList mergeLists(LinkedList * listOne, LinkedList * listTwo) {

  LinkedList result = {.head = NULL};

  if (
    (listOne == NULL && listTwo == NULL) ||
    (listOne->head == NULL && listTwo->head == NULL)
  ) return result;

  Node * p = listOne->head;
  Node * q = listTwo->head;

  if ( (p != NULL && q == NULL) || (p == NULL && q != NULL) ) {

    if (p != NULL) {
      result.head = p;
      listOne->head = NULL;
    }

    if (q != NULL) {
      result.head = q;
      listTwo->head = NULL;
    }

    return result;
  }

  Node * z = p;
  result.head = p;
  p = p->next;
  z->next = q;
  q = q->next;
  z = z->next;
  z->next = NULL;

  while (p != NULL || q != NULL) {

    if (p != NULL) {
      z->next = p;
      z = p;
      p = p->next;
      z->next = NULL;
    }

    if (q != NULL) {
      z->next = q;
      z = q;
      q = q->next;
      z->next = NULL;
    }
  }

  listOne->head = NULL;
  listTwo->head = NULL;

  return result;
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

  LinkedList firstList = {.head=NULL};
  LinkedList secondList = {.head=NULL};

  insertInListAtEnd(&firstList, 111);
  insertInListAtEnd(&firstList, 222);
  insertInListAtEnd(&firstList, 333);

  insertInListAtEnd(&secondList, 444);
  insertInListAtEnd(&secondList, 555);
  insertInListAtEnd(&secondList, 666);
  insertInListAtEnd(&secondList, 777);

  printf("First list\n");
  displayList(&firstList);
  printf("\n");

  printf("Second list\n");
  displayList(&secondList);
  printf("\n");

  LinkedList result = mergeLists(&firstList, &secondList);

  printf("Result\n");
  displayList(&result);
  printf("\n");

  clearListMemory(&firstList);
  clearListMemory(&secondList);
  clearListMemory(&result);

  return 0;
}
