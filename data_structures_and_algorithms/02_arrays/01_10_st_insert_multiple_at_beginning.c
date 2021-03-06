#include <stdio.h>


int main(int argc, char const *argv[]) {
  unsigned int l1[] = {1, 2, 3, 4, 5};

  int new_items[] = {66, 77, 88, 99};

  unsigned int l1_size = sizeof(l1)/sizeof(int);
  unsigned int new_items_size = sizeof(new_items)/sizeof(int);
  unsigned int new_size = l1_size + new_items_size;

  unsigned int l2[new_size];

  // insert multiple at beginning here
  for (int i = 0; i < new_items_size; ++i) {
    // we have to set the origin at l1_size
    // since that's the position of the last item
    // from the first sequence
    l2[i] = new_items[i];
  }

  // the copy of the original sequence goes in range
  // 0 ... l1_size
  for (int i = 0; i < l1_size; ++i) {
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
