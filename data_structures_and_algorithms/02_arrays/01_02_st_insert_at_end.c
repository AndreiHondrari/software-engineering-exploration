#include <stdio.h>


int main(int argc, char const *argv[]) {
  unsigned int l1[] = {1, 2, 3};

  unsigned int l1_size = sizeof(l1)/sizeof(int);
  unsigned int new_size = l1_size + 1;

  unsigned int l2[new_size];

  // Notice that copy of the original goes from 0 ... (l1_size - 1) leaving
  // one element empty at the end
  for (int i = 0; i < l1_size; ++i) {
    l2[i] = l1[i];
  }

  const unsigned int NEW_ELEM = 333;
  l2[new_size - 1] = NEW_ELEM;

  // print before
  printf("BEFORE ");
  for (int i = 0; i < l1_size; ++i) {
    printf("%d ", l1[i]);
  }

  // print after
  printf("\nAFTER  ");
  for (int i = 0; i < new_size; ++i) {
    printf("%d ", l2[i]);
  }

  return 0;
}
