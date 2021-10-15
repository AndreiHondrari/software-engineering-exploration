#include <stdio.h>


int main(int argc, char const *argv[]) {
  unsigned int l1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};

  const unsigned int AMOUNT = 7;

  unsigned int l1_size = sizeof(l1)/sizeof(int);

  unsigned int l2[][AMOUNT];

  // add elements before offset
  for (int i = 0; i < AMOUNT; ++i) {
    l2[i] = l1[i];
  }

  // print before
  printf("BEFORE ");
  for (int i = 0; i < l1_size; ++i) {
    printf("%d ", l1[i]);
  }

  // print after
  printf("\nAFTER  ");
  for (int i = 0; i < AMOUNT; ++i) {
    printf("%d ", l2[i]);
  }

  return 0;
}
