#include <stdio.h>
#include <stdlib.h>
#include <assert.h>


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
  int array1[] = {11, 22, 33, 44, 55};
  int array2[] = {66, 77, 88, 99, 110};

  const int SIZE = sizeof(array1) / sizeof(int);
  const int A2SIZE = sizeof(array2) / sizeof(int);

  assert(SIZE == A2SIZE);

  print_list(array1, SIZE, "A1");
  print_list(array2, SIZE, "A2");

  int array3[SIZE * 2];  // obviously we need double the size

  int i = 0;  // for array3
  int j = 0;  // for array1 and array2
  while (i < SIZE * 2) {
    array3[i] = array1[j];
    ++i;
    array3[i] = array2[j];
    ++i;

    ++j;
  }

  print_list(array3, SIZE * 2, "A3");

  return 0;
}
