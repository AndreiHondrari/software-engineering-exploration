#include <stdarg.h>


void do_something(int n, ...)  // first param required by ISO C
{
  va_list args;  // declares a list of arguments
  va_start(args, n);  // copies the parameters into the args list

  int x = 0;
  for (int i = 0; i < n; i++) {
    x = va_arg(args, int); // extracts the argument and casts it
    printf("%d ", x);
  }
}

int main() {
  do_something(3, 11, 22, 33);
  return 0;
}
