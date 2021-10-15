#include <stdio.h>
#include <stdlib.h>


int main(int argc, char const *argv[]) {
  unsigned int l1[] = {11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 120, 130};
  unsigned int indexes[] = {0, 5, 6, 12};

  const unsigned int L1_SIZE = sizeof(l1)/sizeof(int);
  const unsigned int NEW_SIZE = (int) sizeof(indexes)/sizeof(int);

  unsigned int l2[NEW_SIZE];

  unsigned int p = 0;
  unsigned int current_index;
  for (int i = 0; i < NEW_SIZE; ++i) {
    current_index = indexes[i];
    l2[p] = l1[current_index];
    ++p;
  }

  // print original
  printf("ORIGINAL ");
  for (int i = 0; i < L1_SIZE; ++i) {
    printf("%d ", l1[i]);
  }
  printf("\n");

  // print extracted
  printf("EXTRACTED ");
  for (int i = 0; i < NEW_SIZE; ++i) {
    printf("%d ", l2[i]);
  }
  printf("\n");

  return 0;
}
