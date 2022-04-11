
// Define the "class" body
struct MyClassStruct {
  int a;
} MyClassDefault = {11};  // give defaults

// give it a shorter type name
typedef struct MyClassStruct MyClass;

// create a function for the "class"
void doSomething(MyClass * obj) {
  obj->a *= 2;
}

int main(int argc, char const *argv[]) {
  // instantiate
  MyClass myObj = MyClassDefault;

  // call method
  doSomething(&myObj);

  printf("%d\n", myObj.a);

  return 0;
}
