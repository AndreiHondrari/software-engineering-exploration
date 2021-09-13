#import <iostream>
#import <functional>

using namespace std;


void do_this() {
  cout << "instruction_1" << endl;
  cout << "instruction_2" << endl;
}

void do_that() {
  cout << "instruction_x" << endl;
  cout << "instruction_y" << endl;
}

std::function<void()> wrap(
  void (*wrapee)()
) {
  return [wrapee]() {
    cout << "pre" << endl;
    wrapee();
    cout << "post" << endl << endl;
  };
}

int main(int argc, char const *argv[]) {
  cout << "Call this" << endl;
  std::function<void()> do_wrapped_this = wrap(&do_this);
  do_wrapped_this();

  cout << "Call that" << endl;
  std::function<void()> do_wrapped_that = wrap(&do_that);
  do_wrapped_that();
  return 0;
}
