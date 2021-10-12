/*
Shifting right a number while discarding the right digit can be done by
integer division. In C there is no explicit integer division operator so
instead we just divide by 10 and then cast the result to integer,
discarding the fractional part of the resulting value.
*/
#include <stdio.h>


int main(int argc, char const *argv[]) {
  unsigned int a = 12345;
  unsigned int x = (int) a / 10;
  printf("%d -> %d", a, x);
  return 0;
}
