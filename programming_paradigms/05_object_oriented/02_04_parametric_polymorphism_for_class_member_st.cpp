#include <iostream>

using namespace std;


template <typename T>
class Thing {
  public:
    T k = 0;

    Thing(T k) {
      this->k = k;
    }
};



int main(int argc, char const *argv[]) {
  cout << endl << "# Parametric polymorphism in static languages" << endl;

  Thing<int> t1 = Thing<int>(123);
  Thing<float> t2 = Thing<float>(12.57f);

  cout << "T1: " << t1.k << endl;
  cout << "T2: " << t2.k << endl;

  cout << endl;

  return 0;
}
