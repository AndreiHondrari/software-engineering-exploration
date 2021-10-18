#include <stdio.h>


int main(int argc, char const *argv[]) {
  int l1[] = {11, 22, 33, 44, 55, 66, 77, 88, 99};
  int L1SIZE = sizeof(l1) / sizeof(int);
  int AMOUNT = 3;

  int NEW_SIZE = L1SIZE - AMOUNT;
  int l2[NEW_SIZE];

  for (int i = 0; i < NEW_SIZE; ++i) {
    // the 1+ offset from the original
    // moves the extraction range to the right
    l2[i] = l1[AMOUNT + i];
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
