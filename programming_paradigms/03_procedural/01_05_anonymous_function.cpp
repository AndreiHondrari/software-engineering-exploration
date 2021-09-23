#import <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  // typically you don't assign a lambda to a variable
  auto anonymous_function = [](int x, int y){return x+y;};
  int result = anonymous_function(11, 22);
  cout << result << endl;
  return 0;
}
