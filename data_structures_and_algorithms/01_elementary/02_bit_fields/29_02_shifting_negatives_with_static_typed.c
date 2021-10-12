/*
In the case of C, shifting numbers has different behaviours depending on the
signed/unsigned status of a variable, and also depending on the state
of the sign bit.

Shifting to the right an unsigned variable will simply just move the bits
to the right, discarding the LSB and filling the MSB with 0.

Shifting to the right a signed variable with the sign bit set to 0 will
simply do the same as shifting an unsigned variable.

Shifting to the right a signed variable with the sign bit set to 1 (negative)
the operation will result with the MSB being filled with 1 instead,
so for a full shift right (8 places) you will end up with
0b11111111 in binary or -1 in decimal.
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
  signed char a = 0b10001000;
  unsigned char b = 0b10001000;

  printf("INITIALS\n");
  printf("a %d  ", a);
  print_bits(a);
  printf("\n");

  printf("b  %d  ", b);
  print_bits(b);
  printf("\n");

  // shifting a few places
  a = a >> 2;
  b = b >> 2;
  printf("\nSHIFTED A FEW PLACES\n");
  printf("a %d  ", a);
  print_bits(a);
  printf("\n");

  printf("b  %d  ", b);
  print_bits(b);
  printf("\n");

  // shifting fully
  a = a >> 6;
  b = b >> 6;
  printf("\nSHIFTED FULLY\n");
  printf("a %d  ", a);
  print_bits(a);
  printf("\n");

  printf("b  %d  ", b);
  print_bits(b);
  printf("\n");

  return 0;
}
