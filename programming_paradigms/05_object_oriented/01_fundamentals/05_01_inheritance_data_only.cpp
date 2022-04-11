
#include <iostream>

using namespace std;


class A {
  public:
    int p = 0;
    int q = 0;
};

class B : public A {
  public:
    int x = 0;
    int y = 0;
};


int main(int argc, char const *argv[]) {
  cout << endl << "# Data inheritance" << endl;

  A a = A();
  a.p = 11;
  a.q = 22;
  // a.x = 777;  // will not compile because A does not have x

  B b = B();

  // members from A's definition are accessible due to inheritance
  b.p = 33;
  b.q = 44;

  // members from B's definition
  b.x = 55;
  b.y = 66;

  cout << "B: " << b.p << " " << b.x << endl;

  cout << endl;

  return 0;
}
