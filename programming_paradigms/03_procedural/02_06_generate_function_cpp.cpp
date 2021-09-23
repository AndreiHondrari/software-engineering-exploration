#include <iostream>

using namespace std;

void (*create_function_classically())() {
  return []() {
    cout << "some_classy_instruction" << endl;
  };
}


std::function<void()> create_function_enhanced() {
  return []() {
    cout << "some_enhanced_instruction" << endl;
  };
}

int main(int argc, char const *argv[]) {
  void(*classy_function)() = create_function_classically();
  classy_function();

  std::function<void()> enhanced_function = create_function_enhanced();
  enhanced_function();
  return 0;
}
