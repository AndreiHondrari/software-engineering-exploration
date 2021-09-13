#import <iostream>

using namespace std;


void do_this() {
  cout << "instruction_1" << endl;
  cout << "instruction_2" << endl;
}

void do_that() {
  cout << "instruction_x" << endl;
  cout << "instruction_y" << endl;
}

auto wrap(void (*wrapee)()) {

}

int main(int argc, char const *argv[]) {

  return 0;
}
