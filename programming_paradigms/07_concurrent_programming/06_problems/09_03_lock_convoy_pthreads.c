#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

typedef struct Args {
  unsigned long limit
} Args;

pthread_mutex_t hotLock = PTHREAD_MUTEX_INITIALIZER;

static volatile int k = 0;

void * doWithLock(void * argsPtr) {
  Args args  = *((Args *) argsPtr);
  for (int i = 0; i < args.limit; i++) {
    pthread_mutex_lock(&hotLock);
    k = i;
    pthread_mutex_unlock(&hotLock);
  }
}

void * doLockFree(void * argsPtr) {
    Args args  = *((Args *) argsPtr);

    unsigned int local_k = 0;
    for (int i = 0; i < args.limit; i++) {
      k += 1;
    }
}

void launchFor(
  void * (*func)(),
  char * name,
  unsigned int numberOfThreads,
  unsigned int target
) {
  printf("\n[%s] Launch | %d threads | %d ops\n", name, numberOfThreads, target);
  time_t start, stop;
  double elapsedTime = 0;

  pthread_t threadsArray[numberOfThreads];

  time(&start);

  // CREATE
  Args * args = malloc(sizeof(Args));
  args->limit = target;
  printf("[%s] create threads\n", name);
  for (int i = 0; i < numberOfThreads; ++i) {
    pthread_t newThreadIdent;
    pthread_create(
      &newThreadIdent, // thread ident
      NULL, // thread execution attributes
      func, // routine
      (void *) args  // parameter
    );
    threadsArray[i] = newThreadIdent;
  }

  // WAIT
  printf("[%s] wait for threads\n", name);
  for (int i = 0; i < numberOfThreads; ++i) {
    pthread_join(threadsArray[i], NULL);
  }

  time(&stop);
  elapsedTime = difftime(stop, start);
  printf("[%s] elapsed time %f\n", name, elapsedTime);

  // clean
  free(args);
}

int main(int argc, char const *argv[]) {
  printf("[MAIN] START\n");

  const unsigned int TARGET = 500000;
  launchFor(&doWithLock, "ALFA", 5, TARGET);
  launchFor(&doWithLock, "BRAVO", 24, TARGET);
  launchFor(&doWithLock, "CHARLIE", 128, TARGET);

  launchFor(&doLockFree, "PROXIMA", 5, TARGET);
  launchFor(&doLockFree, "CENTAURI", 24, TARGET);
  launchFor(&doLockFree, "URSA", 128, TARGET);

  printf("[MAIN] STOP\n");
  return 0;
}
