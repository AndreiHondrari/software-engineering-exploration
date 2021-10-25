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

Node * insertAtOffset(
  LinkedList * list,
  unsigned int offset,
  int newValue
) {
  if (list == NULL) return NULL;

  Node * newNode = malloc(sizeof(Node));
  newNode->value = newValue;

  Node * p = list->head;
  Node * q = p;

  // scan first for the node at the offset (or last)
  int i = 0;
  while (p != NULL && i < offset) {
    q = p;
    p = p->next;
    ++i;
  }


  // link element before offset (or last) with new node
  q->next = newNode;
  newNode->prev = q;

  // perform the insertion for last
  if (p == NULL) {
    newNode->next = NULL;
    list->tail = newNode;
  }

  // or otherwise perform the insertion for position
  else {
    newNode->next = p;
    p->prev = newNode;
  }

  return newNode;
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

void displayListBackward(LinkedList * list) {
  if (list == NULL || list->head == NULL) return;
  Node * p = list->tail;
  while (p != NULL) {
    printf("%p { %d }\n", p, p->value);
    p = p->prev;
  }
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

  printf("ORIGINAL\n");
  displayList(&list);

  insertAtOffset(&list, 2, 777);

  printf("FORWARD\n");
  displayList(&list);

  printf("BACKWARD\n");
  displayListBackward(&list);

  clearListMemory(&list);

  return 0;
}
