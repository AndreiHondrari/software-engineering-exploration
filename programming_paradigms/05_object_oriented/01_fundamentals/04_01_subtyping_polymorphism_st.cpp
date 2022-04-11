#include <iostream>
#include <string>

using namespace std;

// base abstract class
class Thing {
  public:
    virtual string getName() = 0;
};

// a concrete class
class A : public Thing {

  public:

    string fullName = "";

    A(string fullName) {
      this->fullName = fullName;
    }

    string getName() {
      return this->fullName;
    };
};

// another concrete class
class B : public Thing {
  public:

    B(string firstName, string lastName) {
      this->firstName = firstName;
      this->lastName = lastName;
    }

    string firstName = "";
    string lastName = "";

    string getName() {
      return firstName + " " + lastName;
    };
};


void printName(Thing * obj) {
  string objName = obj->getName();
  cout << "object's name: " << objName << endl;
};


int main(int argc, char const *argv[]) {
  cout << endl << "# Subtyping" << endl;

  A a = A("Maximus Prime");
  B b = B("Gandalf", "Greybeard");

  printName(&a);
  printName(&b);

  cout << endl;

  return 0;
}
