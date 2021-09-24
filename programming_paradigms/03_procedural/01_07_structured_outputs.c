#include <stdio.h>

typedef struct {
  int a;
  int b;
} Result;


Result obtain_values() {
  Result result = {.a = 11, .b = 22};
  return result;
}

int main(int argc, char const *argv[]) {
  Result result = obtain_values();
  int a = result.a;
  int b = result.b;
  printf("Results: %d %d", a, b);
  return 0;
}
