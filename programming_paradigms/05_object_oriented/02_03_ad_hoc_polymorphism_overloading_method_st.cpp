#include <iostream>

using namespace std;

class Thing {

  public:
    int x = 0;
    int y = 0;

    Thing(int x, int y) {
      this->x = x;
      this->y = y;
    }

    /*
    Ad-hoc Polymorphism below.

    The phenomenon is called "overloading methods".

    The same method name accepts different types as parameters and
    performs different computation based on that.
    */

    void doSomething(int s) {
      this->x = s;
      this->y = s * 10;
    }

    void doSomething(float v) {
      int w = static_cast<int>(v);  // get integer part of the value
      this->x = w * 2;
      this->y = w * 3;
    }
};


int main(int argc, char const *argv[]) {
  cout << endl << "# Ad-hoc polymorphism in static languages" << endl;

  Thing p = Thing(10, 20);

  cout << endl << "Calling doSomething with integer: ";
  p.doSomething(123);
  cout << "p(" << p.x << " " << p.y << ")";

  cout << endl << "Calling doSomething with float: ";
  p.doSomething(7.9f);
  cout << "p(" << p.x << " " << p.y << ")";

  cout << endl;

  return 0;
}
