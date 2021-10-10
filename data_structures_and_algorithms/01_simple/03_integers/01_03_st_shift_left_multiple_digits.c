#include <stdio.h>

int main(int argc, char const *argv[]) {
  unsigned int a = 12345;
  unsigned int amount = 4;

  unsigned int x = a;
  // equivalent to raising of power
  for (int i = 0; i < amount; ++i) {
    x = x * 10;
  }

  printf("%d [%d] -> %d", a, amount, x);
  return 0;
}
