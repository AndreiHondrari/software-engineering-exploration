#include <stdio.h>
#include <math.h>

typedef struct {
  int x;
  int y;
} Context;


void setX(Context * context, int new_x) {
  context->x = new_x;
}

void setY(Context * context, int new_y) {
  context->y = new_y;
}

int calculate_hypothenuse(Context * context) {
  return sqrt(context->x ^ 2 * context->y ^ 2);
}


int main(int argc, char const *argv[]) {
  Context context1;
  Context context2;

  // context 1
  setX(&context1, 11);
  setY(&context1, 22);
  int result1 = calculate_hypothenuse(&context1);
  printf("Result 1: %d\n", result1);

  // context 2
  setX(&context2, 33);
  setY(&context2, 44);
  int result2 = calculate_hypothenuse(&context2);
  printf("Result 2: %d", result2);

  return 0;
}
