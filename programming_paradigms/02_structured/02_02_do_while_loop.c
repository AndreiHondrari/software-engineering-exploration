#include <stdio.h>

int main(int argc, char const *argv[]) {

  int i = 0;

  do {
    printf("instr %d\n", i);
    i += 1;
  } while (i < 3);

  return 0;
}
