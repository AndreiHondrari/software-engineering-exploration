

typedef struct A {
  int x;
  int y;
} A;

typedef struct B {
  int x;
  int y;
  char * name;
} B;


void doSomething(A * obj) {
  obj->x *= 2;
  obj->y *= 2;
};


int main(int argc, char const *argv[]) {

  B o1;
  o1.x = 11;
  o1.y = 1111;
  o1.name = "AAAAA";

  A * o1casted = (A*) &o1;

  doSomething(o1casted);

  printf("%d %d", o1casted->x,  o1casted->y);

  return 0;
}
