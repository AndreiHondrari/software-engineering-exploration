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

  const int L1SIZE = sizeof(l1) / sizeof(int);
  const int L2SIZE = sizeof(l1) / sizeof(int);

  if (L1SIZE != L2SIZE) {
    printf("Arrays must have the same length !");
    exit(1);
  }

  print_list(l1, L1SIZE, "L1");
  print_list(l2, L2SIZE, "L2 BEFORE");

  l2[OFFSET] = l1[OFFSET];  // the actual overwrite

  print_list(l2, L2SIZE, "L2 AFTER");

  return 0;
}
