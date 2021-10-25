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

  insertInListAtEnd(&list, 11);
  insertInListAtEnd(&list, 22);
  insertInListAtEnd(&list, 33);
  insertInListAtEnd(&list, 44);
  insertInListAtEnd(&list, 55);

  printf("Before\n");
  displayList(&list);
  printf("\n");

  Node * node = getNodeAt(&list, 2);
  node->value = 777;

  printf("After\n");
  displayList(&list);
  printf("\n");

  clearListMemory(&list);

  return 0;
}
