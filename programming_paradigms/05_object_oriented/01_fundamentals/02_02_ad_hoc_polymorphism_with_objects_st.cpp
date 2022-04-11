#include <iostream>

using namespace std;

class A {

  public:
    int x = 0;
    int y = 0;

    A(int x, int y) {
      this->x = x;
      this->y = y;
    }
};


class B {

  public:
    int k = 0;
    int m = 0;

    B(int k, int m) {
      this->k = k;
      this->m = m;
    }
};


/*
Ad-hoc Polymorphism below.

The phenomenon is called "overloading functions".

The same function name accepts different types as parameters and
performs different computation based on that.
*/

int addMembers(A obj) {
  return obj.x + obj.y;
}

int addMembers(B obj) {
  return obj.k + obj.m;
}


int main(int argc, char const *argv[]) {
  cout << endl << "# Ad-hoc polymorphism in static languages" << endl;

  A p = A(10, 20);
  B q = B(55, 77);

  cout << endl << "Adding members for p(" << p.x << " " << p.y << ") -> ";
  int res1 = addMembers(p);
  cout << res1 << endl;

  cout << endl << "Adding members for q(" << q.k << " " << q.m << ") -> ";
  int res2 = addMembers(q);
  cout << res2 << endl;

  cout << endl;

  return 0;
}
