#include <stdio.h>

int * obtain_values() {
  static int results[2] = {1, 2};
  return results;
}


int main(int argc, char const *argv[]) {
  int * results = obtain_values();
  int a = results[0];
  int b = results[1];
  printf("Results: %d %d", a, b);
  return 0;
}
