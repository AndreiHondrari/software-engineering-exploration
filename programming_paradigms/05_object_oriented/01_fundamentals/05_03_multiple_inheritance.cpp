
#include <iostream>
#include <string>

using namespace std;


class A {
  public:

    void doThis() {
      cout << "Doing T H I S" << endl;
    }
};

class B {

  public:

    void doThat() {
      cout << "Doing T H A T" << endl;
    }

};

class X: public A, public B {};


int main(int argc, char const *argv[]) {
  cout << endl << "# Multiple inheritance" << endl << endl;

  X x = X();
  x.doThis();
  x.doThat();

  cout << endl;

  return 0;
}
