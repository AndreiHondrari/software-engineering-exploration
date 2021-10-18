#include <stdio.h>


int main(int argc, char const *argv[]) {
  int l1[] = {11, 22, 33, 44, 55, 66, 77, 88, 99};
  int L1SIZE = sizeof(l1) / sizeof(int);
  int OFFSET = 4;
  int AMOUNT = 3;

  int NEW_SIZE = L1SIZE - AMOUNT;
  int l2[NEW_SIZE];

  // copy before offset
  for (int i = 0; i < OFFSET; ++i) {
    l2[i] = l1[i];
  }

  // copy after offset
  for (int i = OFFSET + AMOUNT; i < L1SIZE; ++i) {
    // - AMOUNT to counteract the position difference of the offset
    l2[i - AMOUNT] = l1[i];
  }


  // print original
  printf("L1: ");
  for (int i = 0; i < L1SIZE; ++i) {
    printf("%d ", l1[i]);
  }
  printf("\n");

  // print extracted
  printf("L2: ");
  for (int i = 0; i < NEW_SIZE; ++i) {
    printf("%d ", l2[i]);
  }
  printf("\n");

  return 0;
}
