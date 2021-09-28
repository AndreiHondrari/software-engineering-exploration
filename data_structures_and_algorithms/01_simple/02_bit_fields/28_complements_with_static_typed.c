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
  signed char a = 0b00010001;
  unsigned char b = 0b00010001;

  printf("INITIALS\n");
  printf("a  %d ", a);
  print_bits(a);
  printf("\n");

  printf("b  %d ", b);
  print_bits(b);
  printf("\n");

  // one's complement
  a = ~a;
  b = ~b;

  printf("\nOne's complement\n");
  printf("a %d ", a);
  print_bits(a);
  printf("\n");

  printf("b %d ", b);
  print_bits(b);
  printf("\n");

  // two's complement
  a = a + 1;
  b = a + 1;

  printf("\nTwo's complement\n");
  printf("a %d ", a);
  print_bits(a);
  printf("\n");

  printf("b %d ", b);
  print_bits(b);
  printf("\n");

  return 0;
}
