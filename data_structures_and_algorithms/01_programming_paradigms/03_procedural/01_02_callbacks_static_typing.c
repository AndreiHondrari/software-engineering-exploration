#include <stdio.h>

void do_something(
  void (*some_function)()
) {
  printf("pre\n");  // pre operation
  some_function();  // infix operation / callback call
  printf("post\n");  // post operation
}

void do_this() {
  printf("instruction_1\n");
  printf("instruction_2\n");
}

void do_that() {
  printf("instruction_x\n");
  printf("instruction_y\n");
}


int main(int argc, char const *argv[]) {
  printf("Call this\n");
  do_something(&do_this);

  printf("\nCall that\n");
  do_something(&do_that);

  return 0;
}
