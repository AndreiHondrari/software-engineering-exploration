#include <iostream>
#include <thread>
#include <string>

using namespace std;


void doSomething(string name) {
  char buffer[100];

  sprintf(buffer, "[%s] START", name.c_str());
  cout << buffer << endl;

  sprintf(buffer, "[%s] STOP", name.c_str());
  cout << buffer << endl;
}


int main(int argc, char const *argv[]) {
  cout << endl << "[MAIN] START" << endl;

  thread someThread = thread(doSomething, "maximus");

  someThread.join();

  cout << "[MAIN] STOP" << endl << endl;
  return 0;
}
