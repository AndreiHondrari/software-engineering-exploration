#include <stdio.h>
#include <stdlib.h>


int main(int argc, char const *argv[]) {
  unsigned int l1[] = {11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 120, 130};
  const unsigned char N_OFFSET = 3;

  if (N_OFFSET == 0) {
    printf("N offset must be positive non-zero value");
    exit(1);
  }

  const unsigned int L1_SIZE = sizeof(l1)/sizeof(int);
  const unsigned int NEW_SIZE = (int) (L1_SIZE / N_OFFSET);

  unsigned int l2[NEW_SIZE];

  unsigned int p = 0;
  for (int i = N_OFFSET - 1; i < L1_SIZE; i = i + N_OFFSET) {
    l2[p] = l1[i];
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
