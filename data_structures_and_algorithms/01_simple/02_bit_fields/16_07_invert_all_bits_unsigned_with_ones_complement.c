/*
Invert all bits in a static typed language.
Signed variable.
*/

#include <stdio.h>

void print_bits(int x) {
  // just for printing the bits
  for (int i = 7; i >= 0; --i) {
    char is_zero = ((x >> i) & 0b1) == 0;
    printf("%c", (is_zero ? '0' : '1'));
  }
}

int main(int argc, char const *argv[]) {
  // define a value
  unsigned char a = 0b00001111;

  printf("%d  ", a);
  print_bits(a);
  printf("\n");

  // invert the bits
  a = ~a;

  printf("%d ", a);
  print_bits(a);
  printf("\n");

  return 0;
}
