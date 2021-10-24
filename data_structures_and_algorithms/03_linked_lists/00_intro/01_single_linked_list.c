#include <stdio.h>


typedef struct Node {
  int value;
  struct Node * next;
} Node;

#define NODE_DEFAULT {.next = NULL}


int main(int argc, char const *argv[]) {
  Node n1 = NODE_DEFAULT;
  Node n2 = NODE_DEFAULT;
  Node n3 = NODE_DEFAULT;
  Node n4 = NODE_DEFAULT;

  // incidentally n1 is the head of the linked list
  n1.value = 11;
  n1.next = &n2;

  n2.value = 22;
  n2.next = &n3;

  n3.value = 33;
  n3.next = &n4;

  n4.value = 44;

  Node * p = &n1;
  while (p != NULL) {
    printf("%p: %d\n", p, p->value);
    p = p->next;
  }

  return 0;
}
