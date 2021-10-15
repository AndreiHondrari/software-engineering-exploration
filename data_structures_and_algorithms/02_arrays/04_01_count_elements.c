#include <stdio.h>

int main(int argc, char const *argv[]) {

  unsigned int l1[] = {11, 22, 33, 44, 55};

  unsigned short int L1_SIZE = (int) sizeof(l1)/sizeof(int);

  // print original
  printf("ORIGINAL ");
  for (int i = 0; i < L1_SIZE; ++i) {
    printf("%d ", l1[i]);
  }
  printf("\n");

  printf("SIZE: %d\n", L1_SIZE);

  return 0;
}
