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

unsigned int getListSize(LinkedList * list) {
  unsigned int result = 0;

  Node * p = list->head;
  while (p != NULL) {
    result += 1;
    p = p->next;
  }

  return result;
}

LinkedList cloneList(LinkedList * list) {
  LinkedList result = {.head=NULL};

  if (list == NULL || list->head == NULL) return result;

  Node * p = list->head;
  while (p != NULL) {
    insertInListAtEnd(&result, p->value);
    p = p->next;
  }

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

  LinkedList list = {.head=NULL};

  int values[] = {55, 22, 33, 77};
  unsigned int SIZE = sizeof(values) / sizeof(int);

  for (int i = 0; i < SIZE; ++i) {
    insertInListAtEnd(&list, values[i]);
  }

  printf("Before\n");
  displayList(&list);
  printf("\n");

  LinkedList listCopy = cloneList(&list);

  printf("After\n");
  displayList(&listCopy);
  printf("\n");

  clearListMemory(&list);
  clearListMemory(&listCopy);

  return 0;
}
