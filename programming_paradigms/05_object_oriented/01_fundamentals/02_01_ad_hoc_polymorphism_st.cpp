#include <iostream>

using namespace std;

/*
Ad-hoc Polymorphism below.

The phenomenon is called "overloading functions".

The same function name accepts different types as parameters and
performs different computation based on that.
*/

int doSomething(int x) {
  return 11 * x;
}

long doSomething(int a, int b) {
  return a * 100 * b;
}

float doSomething(float k) {
  int integralPart = static_cast<int>(k);
  float fractionaryPart = k - integralPart;
  return integralPart * 2 + fractionaryPart / 10;
}


int main(int argc, char const *argv[]) {
  cout << endl << "# Ad-hoc polymorphism in static languages" << endl;

  int res1 = doSomething(7);
  cout << "Res 1: " << res1 << endl;

  int res2 = doSomething(5, 9);
  cout << "Res 2: " << res2 << endl;

  float res3 = doSomething(12.57f);
  cout << "Res 3: " << res3 << endl;

  cout << endl;

  return 0;
}
