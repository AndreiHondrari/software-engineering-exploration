
#include <iostream>
#include <string>

using namespace std;


class A {
  public:
    string name = "";

    void doSomething() {
      cout << this->name << " does something ..." << endl;
    }
};

class B : public A {
};


int main(int argc, char const *argv[]) {
  cout << endl << "# Functionality inheritance" << endl << endl;

  B b = B();
  b.name = "Gandalf";
  b.doSomething();  // works because B inherits doSomething from A

  cout << endl;

  return 0;
}
