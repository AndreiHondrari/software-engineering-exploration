#import <iostream>

using namespace std;

// T will be whatever type we want our arguments to have
// Args is just a given type name for the args, it can be anything
template <typename T, typename... Args>
void do_something(Args... args) {

  int n = sizeof...(Args);  // we get the size of all the arguments
  T arr[] = {args...};  // we unpack the parameters into an array

  // we iterate over the parameters
  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";  // and do something with them
  }
  cout << endl;
}

int main() {
  do_something<int>(11, 22, 33);
  do_something<int>(77, 88);
  return 0;
}
