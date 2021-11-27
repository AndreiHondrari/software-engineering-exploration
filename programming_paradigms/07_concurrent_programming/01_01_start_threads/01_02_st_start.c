#include <stdio.h>
#include <pthread.h>


void * doSomething(void * arg) {
  char * name = (char *) arg;
  printf("[%s] START\n", name);

  pthread_t tid = pthread_self();

  printf("---------------\n");
  printf("[%s] IDENT: %lu\n", name, tid);
  printf("---------------\n");

  printf("[%s] STOP\n", name);
}


int main(int argc, char const *argv[]) {
  int rc = 0;

  pthread_t someThreadIdent;
  char * name = "maximus";

  rc = pthread_create(
    &someThreadIdent, // thread ident
    NULL, // thread execution attributes
    &doSomething, // routine
    (void *) name  // parameter
  );
  printf("[MAIN] pthread_create rc: %d\n", rc);



  pthread_join(someThreadIdent, NULL);

  printf("[MAIN] STOP\n");
  return 0;
}
