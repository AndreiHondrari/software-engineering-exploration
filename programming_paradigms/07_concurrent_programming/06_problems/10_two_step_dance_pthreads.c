/*

*/
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
#include <unistd.h>

const float STANDARD_PROCCESS_TIME = 0.01;

typedef struct Args {
  unsigned long limit;
} Args;

pthread_mutex_t hotLock = PTHREAD_MUTEX_INITIALIZER;

pthread_mutex_t condLock = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;

static volatile int k = 0;

void * doInnocent(void * argsPtr) {
  Args args = *((Args *) argsPtr);
  for (int i = 0; i < args.limit; ++i) {
    pthread_cond_wait(&cond, &condLock);
    pthread_mutex_lock(&hotLock);
    pthread_mutex_unlock(&hotLock);
  }
}

void * doSuboptimal(void * argsPtr) {
  printf("[SUBOPTIMAL] START\n");
  fflush(stdout);
  Args args = *((Args *) argsPtr);

  for (int i = 0; i < args.limit; ++i) {
    // first lock
    pthread_mutex_lock(&hotLock);

    // then signal
    pthread_cond_signal(&cond);

    // then unlock
    pthread_mutex_unlock(&hotLock);

    sleep(STANDARD_PROCCESS_TIME);
  }

  printf("[SUBOPTIMAL] DONE\n");
  fflush(stdout);
}

void * doOptimal(void * argsPtr) {
  printf("[OPTIMAL] START\n");
  fflush(stdout);
  Args args = *((Args *) argsPtr);

  for (int i = 0; i < args.limit; ++i) {
    // first lock
    pthread_mutex_lock(&hotLock);

    // then unlock
    pthread_mutex_unlock(&hotLock);

    // then signal
    pthread_cond_signal(&cond);

    sleep(STANDARD_PROCCESS_TIME);
  }
  printf("[OPTIMAL] DONE\n");
  fflush(stdout);
}

void launchFor(
  void * (*innocent)(),
  void * (*perpetrator)(),
  char * name,
  unsigned int target
) {
  printf("\n[%s] Launch | %d ops\n", name, target);
  time_t start, stop;
  double elapsedTime = 0;

  pthread_t innocentThread, perpetratorThread;

  time(&start);

  // CREATE
  Args * args = malloc(sizeof(Args));
  args->limit = target;

  printf("[%s] create threads\n", name);

  pthread_create(
    &innocentThread, // thread ident
    NULL, // thread execution attributes
    innocent, // routine
    (void *) args  // parameter
  );

  pthread_create(
    &perpetratorThread, // thread ident
    NULL, // thread execution attributes
    perpetrator, // routine
    (void *) args  // parameter
  );


  // WAIT
  printf("[%s] wait for threads\n", name);
  pthread_join(perpetratorThread, NULL);

  time(&stop);
  elapsedTime = difftime(stop, start);
  printf("[%s] elapsed time %f\n", name, elapsedTime);

  // clean
  free(args);
}

int main(int argc, char const *argv[]) {
  printf("[MAIN] START\n");

  const unsigned int TARGET = 100000;
  launchFor(&doInnocent, &doSuboptimal, "ALFA", TARGET);
  launchFor(&doInnocent, &doOptimal, "BRAVO", TARGET);
  printf("[MAIN] STOP\n");
  return 0;
}
