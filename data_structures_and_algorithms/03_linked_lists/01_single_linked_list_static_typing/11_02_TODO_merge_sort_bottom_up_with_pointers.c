"""
TODO !!!!
"""

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

// unsigned int getListSize(LinkedList * list) {
//   unsigned int result = 0;
//
//   Node * p = list->head;
//   while (p != NULL) {
//     result += 1;
//     p = p->next;
//   }
//
//   return result;
// }

// LinkedList cloneList(LinkedList * list) {
//   LinkedList result = {.head=NULL};
//
//   if (list == NULL || list->head == NULL) return result;
//
//   Node * p = list->head;
//   while (p != NULL) {
//     insertInListAtEnd(&result, p->value);
//     p = p->next;
//   }
//
//   return result;
// }

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

LinkedList mergeInOrder(
  LinkedList * listOne,
  LinkedList * listTwo
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
      (q == NULL || (p->value < q->value))
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

LinkedList mergeSort(LinkedList * list) {
  LinkedList result = {.head=NULL};
  if (LIST_SIZE == 0) return result;

  result = cloneList(list);

  if (LIST_SIZE == 1) return result;


  return result;

}

int main(int argc, char const *argv[]) {

  LinkedList list = {.head=NULL};

  int values[] = {7, 2, 10, 1, 9, 6, 3, 4, 8, 5};
  unsigned int SIZE = sizeof(values) / sizeof(int);

  for (int i = 0; i < SIZE; ++i) {
    insertInListAtEnd(&list, values[i]);
  }

  printf("Before\n");
  displayList(&list);
  printf("\n");

  LinkedList sortedList = mergeSort(&list);

  printf("After\n");
  displayList(&sortedList);
  printf("\n");

  clearListMemory(&list);
  clearListMemory(&sortedList);

  return 0;
}
