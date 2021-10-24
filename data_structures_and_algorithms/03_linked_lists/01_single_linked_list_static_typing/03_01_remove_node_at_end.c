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

void removeLastNode(LinkedList * list) {
  if (list == NULL) return;

  Node * toRemove = NULL;

  // obtain last node
  Node * p = list->head;

  if (p->next == NULL) {
    toRemove = p;
    list->head = NULL;
  }

  else {
    Node * q = NULL;
    while (p->next != NULL) {
      q = p;
      p = p->next;
    }

    q->next = NULL; // Remove the link from the pre-last node
    toRemove = p;
  }

  // remove it
  if (toRemove != NULL) {
    free(toRemove);
  }
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

  removeLastNode(&list);

  printf("After\n");
  displayList(&list);
  printf("\n");

  unsigned int size = getListSize(&list);

  printf("size: %d\n", size);

  clearListMemory(&list);

  return 0;
}
