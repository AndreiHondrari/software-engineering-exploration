#include <stdio.h>


int main(int argc, char const *argv[]) {
  unsigned short a = 0b00110101;

  char bits[9] = "";  // 8 bits plus the null character

  for (int i = 0; i < 8; ++i) {
    // extract nth bit
    unsigned short nth_bit = (a >> i) & 0b1;

    // 7-i to go from right to left
    if (nth_bit != 0b0) {
      bits[7-i] = '1';
    } else {
      bits[7-i] = '0';
    }
  }

  printf("%s", bits);

  return 0;
}
