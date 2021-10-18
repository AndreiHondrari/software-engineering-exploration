#include <stdio.h>
#include <stdlib.h>


void print_list(
  int array[],
  int array_size,
  char * description
) {
  printf("%s: ", description);

  for (int i = 0; i < array_size; ++i) {
    printf("%d ", array[i]);
  }

  printf("\n");
}


int main(int argc, char const *argv[]) {
  int l1[] = { 11, 22, 33, 44, 55  };
  int l2[] = { 66, 77, 88, 99, 110 };
  const int OFFSET = 2;

  const int SIZE = sizeof(l1) / sizeof(int);
  const int L2SIZE = sizeof(l1) / sizeof(int);

  if (SIZE != L2SIZE) {
    printf("Arrays must have the same length !");
    exit(1);
  }

  print_list(l1, SIZE, "L1");
  print_list(l2, SIZE, "L2");

  int l3[SIZE];
  for (int i = 0; i < SIZE; ++i) {
    if (i == OFFSET) {
      l3[i] = l2[i];
    }
    else {
      l3[i] = l1[i];
    }
  }

  print_list(l3, SIZE, "L3");

  return 0;
}
