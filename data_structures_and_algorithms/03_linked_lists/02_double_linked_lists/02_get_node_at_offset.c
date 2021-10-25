#include <stdlib.h>
#include <stdio.h>

typedef struct Node {
  int value;
  struct Node * prev;
  struct Node * next;
} Node;

typedef struct LinkedList {
  struct Node * head;
  struct Node * tail;
} LinkedList;

Node * insertNodeAtEnd(LinkedList * list, int newValue) {
  if (list == NULL) return NULL;

  Node * newNode = malloc(sizeof(Node));
  newNode->value = newValue;

  if (list->tail == NULL) {
    newNode->prev = NULL;
    newNode->next = NULL;
    list->head = newNode;
  } else {
    list->tail->next = newNode;
    newNode->prev = list->tail;
  }

  list->tail = newNode;

  return newNode;
}

Node * getNodeAtOffset(LinkedList * list, unsigned int offset) {
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
  if (list == NULL || list->head == NULL) return;
  Node * p = list->head;
  while (p != NULL) {
    printf("%p { %d }\n", p, p->value);
    p = p->next;
  }
  printf("\n");
}

void displayNode(Node * node, char * descr) {
  printf("%s\n", descr);
  if (node == NULL) printf("No node");
  else printf("%p { %d }\n", node, node->value);
  printf("\n");
}

void clearListMemory(LinkedList * list) {
  if (list == NULL || list->head == NULL) return;

  Node * p = list->head;
  Node * pNext = p->next;
  while (p != NULL) {
    pNext = p->next;
    free(p);
    p = pNext;
  }
}

int main(int argc, char const *argv[]) {
  LinkedList list = {.head = NULL};

  insertNodeAtEnd(&list, 11);
  insertNodeAtEnd(&list, 22);
  insertNodeAtEnd(&list, 33);
  insertNodeAtEnd(&list, 44);
  insertNodeAtEnd(&list, 55);

  displayList(&list);

  Node * firstNode = getNodeAtOffset(&list, 0);
  Node * someNode = getNodeAtOffset(&list, 2);

  displayNode(firstNode, "FIRST");
  displayNode(someNode, "SOME");

  clearListMemory(&list);

  return 0;
}
