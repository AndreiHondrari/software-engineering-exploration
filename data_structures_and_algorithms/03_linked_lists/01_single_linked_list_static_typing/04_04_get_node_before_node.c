#include <stdio.h>
#include <stdlib.h>


typedef struct Node {
  int value;
  struct Node * next;
} Node;


typedef struct LinkedList {
  Node * head;
} LinkedList;


Node * insertInListAtEnd(LinkedList * list, int newValue) {
  if (list == NULL) return NULL;

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

  return newNode;
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

void displayList(LinkedList * list) {
  if (list == NULL) return;

  Node * p = list->head;
  while (p != NULL) {
    printf("%p { %d } -> %p \n", p, p->value, p->next);
    p = p->next;
  }
}

void displayNode(Node * node, char * descr) {
  printf("%s\n", descr);
  if (node != NULL) printf("%p { %d }\n", node, node->value);
  else printf("No node\n");
  printf("\n");
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

  Node * firstTarget = insertInListAtEnd(&list, 111);
  insertInListAtEnd(&list, 222);
  insertInListAtEnd(&list, 333);
  Node * secondTarget = insertInListAtEnd(&list, 444);
  Node * lastTarget = insertInListAtEnd(&list, 555);

  displayList(&list);
  printf("\n");


  Node * node1 = getNodeBefore(&list, firstTarget);
  displayNode(node1, "FIRST");

  Node * node2 = getNodeBefore(&list, secondTarget);
  displayNode(node2, "SECOND");

  Node * node3 = getNodeBefore(&list, lastTarget);
  displayNode(node3, "LAST");

  clearListMemory(&list);

  return 0;
}
