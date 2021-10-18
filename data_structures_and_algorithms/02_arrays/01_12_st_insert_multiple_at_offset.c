#include <stdio.h>


int main(int argc, char const *argv[]) {
  unsigned int l1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};

  int new_items[] = {66, 77, 88, 99};
  const unsigned int OFFSET = 6;

  unsigned int l1_size = sizeof(l1)/sizeof(int);
  unsigned int new_items_size = sizeof(new_items)/sizeof(int);
  unsigned int new_size = l1_size + new_items_size;

  unsigned int l2[new_size];

  // add elements before offset
  for (int i = 0; i < OFFSET; ++i) {
    l2[i] = l1[i];
  }

  // add elements at offset
  for (int i = 0; i < new_items_size; ++i) {
    l2[OFFSET + i] = new_items[i];
  }

  // add the rest of the elements
  for (int i = OFFSET; i < l1_size; ++i) {
    l2[new_items_size + i] = l1[i];
  }

  // print before
  printf("BEFORE ");
  for (int i = 0; i < l1_size; ++i) {
    printf("%d ", l1[i]);
  }

  // print after
  printf("\nAFTER  ");
  for (int i = 0; i < new_size; ++i) {
    printf("%d ", l2[i]);
  }

  return 0;
}
