#include <iostream>

using namespace std;

auto create_function() {
  return []() {
    cout << "some_instruction" << endl;
  };
}

int main(int argc, char const *argv[]) {
  auto my_function = create_function();
  my_function();
  return 0;
}
