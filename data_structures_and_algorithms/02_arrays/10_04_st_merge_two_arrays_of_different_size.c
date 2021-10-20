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
  int array1[] = {11, 22, 33};
  int array2[] = {44, 55, 66, 77, 88, 99};

  const int A1SIZE = sizeof(array1) / sizeof(int);
  const int A2SIZE = sizeof(array2) / sizeof(int);
  const int NEW_SIZE = A1SIZE + A2SIZE;
  assert(A1SIZE != A2SIZE);

  print_list(array1, A1SIZE, "A1");
  print_list(array2, A2SIZE, "A2");

  // obviously we need the accumulation of the sizes
  int array3[NEW_SIZE];

  int i = 0;  // for array3
  int j = 0;  // for array1 and array2
  while (j < A1SIZE || j < A2SIZE) {
    if (j < A1SIZE) {
      array3[i] = array1[j];
      ++i;
    }

    if (j < A2SIZE) {
      array3[i] = array2[j];
      ++i;
    }

    ++j;
  }

  print_list(array3, NEW_SIZE, "A3");

  return 0;
}
