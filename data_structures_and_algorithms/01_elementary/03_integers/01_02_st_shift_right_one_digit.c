#include <stdio.h>


int main(int argc, char const *argv[]) {
  unsigned int a = 12345;
  unsigned int x = (int) a / 10;
  printf("%d -> %d", a, x);
  return 0;
}
