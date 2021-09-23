#include <stdio.h>

void do_something() {
  printf("some_instruction\n");
}

void (*
  give_function()  // our actual function definition
)() {
  return &do_something;
}

int main(int argc, char const *argv[]) {
  // store function in a pointer variable
  void (*some_function)() = give_function();

  // call the stored function
  (*some_function)();
  
  return 0;
}
