#import <iostream>

using namespace std;

typedef struct {
  int x;
  int y;
  int z;
  int r;
  int g;
  int b;
  int alpha;
  int frame;
} DoSomethingKwargs;

void do_something(DoSomethingKwargs kwargs) {
  // we can access like kwargs.argument_name
  // instructions that use kwargs
  cout << "R " << (kwargs.r / 100.0) * kwargs.alpha
       << " G " << (kwargs.g / 100.0) * kwargs.alpha
       << " B " << (kwargs.b / 100.0) * kwargs.alpha << endl;

  int position = kwargs.x + kwargs.y + kwargs.z;
  cout << "Position " << position << endl;
}

int main() {
  DoSomethingKwargs kwargs = {
    .x=10, .y=25, .z=12,
    .r=255, .g=0, .b=0, .alpha=100,
    .frame=55221521
  };
  do_something(kwargs);
  return 0;
}
