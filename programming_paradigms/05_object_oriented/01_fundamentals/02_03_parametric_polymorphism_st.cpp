#include <iostream>

using namespace std;


class Thing {
  public:
    int k = 0;

    Thing(int k) {
      this->k = k;
    }

    Thing operator + (Thing other) {
      return Thing(this->k + other.k);
    }

    Thing operator * (int factor) {
      return Thing(this->k * factor);
    }
};


template <typename T>
T doSomething(T a, T b) {
  T v = a + b;
  return v * 100;
}


int main(int argc, char const *argv[]) {
  cout << endl << "# Parametric polymorphism in static languages" << endl;
  
  int res1 = doSomething<int>(11, 20);
  cout << "Res 1: " << res1 << endl;

  float res2 = doSomething<float>(12.5789, 2.1);
  cout << "Res 2: " << to_string(res2) << endl;

  Thing p = Thing(2);
  Thing q = Thing(3);
  Thing z = doSomething<Thing>(p, q);
  cout << "Res 3: " << z.k << endl;

  cout << endl;

  return 0;
}
