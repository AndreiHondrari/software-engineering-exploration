#include <stdio.h>
#include <stdlib.h>


typedef struct Node {
  int value;
  struct Node * next;
} Node;


typedef struct LinkedList {
  Node * head;
} LinkedList;

typedef struct SplitLinkedList {
  LinkedList left;
  LinkedList right;
} SplitLinkedList;


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

SplitLinkedList splitList(
  LinkedList * list,
  unsigned int offset
) {
  LinkedList leftList = {.head=NULL};
  LinkedList rightList = {.head=NULL};
  SplitLinkedList result = {.left=leftList, .right=rightList};

  if (list == NULL || list->head == NULL) return result;

  Node * p = list->head;
  Node * x = NULL;
  Node * y = NULL;

  int k = 0;
  while (p != NULL) {

    // to the left
    if (k < offset) {
      if (leftList.head == NULL) {
        leftList.head = p;
        x = p;
      }
      else {
        x->next = p;
        x = p;
      }
    }

    // to the right
    else {
      if (rightList.head == NULL) {
        rightList.head = p;
        y = p;
      }
      else {
        y->next = p;
        y = p;
      }
    }

    p = p->next;
    ++k;
  }

  // close-up the lists
  x->next = NULL;
  y->next = NULL;

  // if (p == NULL) return NULL;
  result.left = leftList;
  result.right = rightList;
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

  insertInListAtEnd(&list, 111);
  insertInListAtEnd(&list, 222);
  insertInListAtEnd(&list, 333);
  insertInListAtEnd(&list, 444);
  insertInListAtEnd(&list, 555);
  insertInListAtEnd(&list, 666);
  insertInListAtEnd(&list, 777);

  printf("Original\n");
  displayList(&list);
  printf("\n");

  SplitLinkedList resultingLists = splitList(&list, 3);
  LinkedList leftList = resultingLists.left;
  LinkedList rightList = resultingLists.right;

  printf("Left list\n");
  displayList(&leftList);
  printf("\n");

  printf("Right list\n");
  displayList(&rightList);
  printf("\n");

  clearListMemory(&list);
  clearListMemory(&leftList);
  clearListMemory(&rightList);

  return 0;
}
