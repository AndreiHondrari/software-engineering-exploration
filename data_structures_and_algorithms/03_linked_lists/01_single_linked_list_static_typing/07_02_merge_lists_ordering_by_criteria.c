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

LinkedList mergeListsByCriteria(
  LinkedList * listOne,
  LinkedList * listTwo,
  unsigned char (*compareFunc)()
) {
  LinkedList result = {.head=NULL};

  if (
    (listOne == NULL && listTwo == NULL) ||
    (listOne->head == NULL && listTwo->head == NULL)
  ) return result;

  Node * p = listOne->head;
  Node * q = listTwo->head;

  while (p != NULL || q != NULL) {
    if (p != NULL &&
      (q == NULL || compareFunc(p->value, q->value))
    ) {
      insertInListAtEnd(&result, p->value);
      p = p->next;
    }
    else {
      insertInListAtEnd(&result, q->value);
      q = q->next;
    }
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

unsigned char lessThan(int a, int b) {
  return a < b;
}

int main(int argc, char const *argv[]) {

  LinkedList firstList = {.head=NULL};
  LinkedList secondList = {.head=NULL};

  insertInListAtEnd(&firstList, 11);
  insertInListAtEnd(&firstList, 44);
  insertInListAtEnd(&firstList, 777);

  insertInListAtEnd(&secondList, 22);
  insertInListAtEnd(&secondList, 33);
  insertInListAtEnd(&secondList, 888);
  insertInListAtEnd(&secondList, 999);

  printf("First list\n");
  displayList(&firstList);
  printf("\n");

  printf("Second list\n");
  displayList(&secondList);
  printf("\n");

  LinkedList result = mergeListsByCriteria(
    &firstList, &secondList, &lessThan
  );

  printf("Result\n");
  displayList(&result);
  printf("\n");

  clearListMemory(&firstList);
  clearListMemory(&secondList);
  clearListMemory(&result);

  return 0;
}
