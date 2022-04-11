
#define BASE_DEFAULT { .x = 111 }

typedef struct {
  int x;
} Base;

typedef struct {
  int x;
} A;

typedef struct {
  int x;
} B;

void f1(Base * obj, void (*doSomething)(Base *)) {
  doSomething(obj);
}

void A__doSomething(Base * self) {
  self->x *= 5;
}

void B__doSomething(Base * self) {
  self->x *= 7;
}

int main(int argc, char const *argv[]) {
  A o1 = BASE_DEFAULT;
  B o2 = BASE_DEFAULT;

  f1((Base *) &o1, &A__doSomething);
  f1((Base *) &o2, &B__doSomething);

  printf("%d %d", o1.x, o2.x);

  return 0;
}
