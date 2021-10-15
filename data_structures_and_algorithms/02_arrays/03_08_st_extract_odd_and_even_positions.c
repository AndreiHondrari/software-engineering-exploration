#include <stdio.h>


int main(int argc, char const *argv[]) {
  unsigned int l1[] = {0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 100};

  const unsigned int L1_SIZE = sizeof(l1)/sizeof(int);
  const unsigned char IS_L1_SIZE_EVEN = L1_SIZE % 2 == 0;
  const unsigned int EVEN_SIZE = (int) (
    (L1_SIZE / 2) + ((IS_L1_SIZE_EVEN) ? 0 : 1)
  );
  const unsigned int ODD_SIZE = (int) (L1_SIZE / 2);

  unsigned int l2[EVEN_SIZE];
  unsigned int l3[ODD_SIZE];

  unsigned int p = 0;
  unsigned int q = 0;
  unsigned int next_i = 0;
  for (int i = 0; i < L1_SIZE; i = i + 2) {
    // evens
    l2[p] = l1[i];
    ++p;

    // odds
    // usually the odd numbers can be extra from a given position
    // considering that we are incrementing in twos
    next_i = i + 1;
    if (next_i < L1_SIZE) {
      l3[q] = l1[next_i];
      ++q;
    }
  }

  // print original
  printf("ORIGINAL ");
  for (int i = 0; i < L1_SIZE; ++i) {
    printf("%d ", l1[i]);
  }
  printf("\n");

  // print evens
  printf("EVENS     ");
  for (int i = 0; i < EVEN_SIZE; ++i) {
    printf("%d ", l2[i]);
  }
  printf("\n");

  // print odds
  printf("ODDS    ");
  for (int i = 0; i < ODD_SIZE; ++i) {
    printf("%d ", l3[i]);
  }
  printf("\n");

  return 0;
}
