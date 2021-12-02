#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>


long k = 0;

// 0x FFFF FFFF FFFF FFFF

void * doWrite(void * arg) {
  printf("[WRITER] START\n");

  unsigned char flip = 0;
  while (1) {
    if (flip) {
      k = 0x0aaabbbbccddeeff;
    } else {
      k = 0;
    }

    flip = !flip;
  }

  printf("[WRITER] STOP\n");
}

void * doRead(void * arg) {
  printf("[READER] START\n");

  while (1) {
    if (!(k == 0 || k == 0x0aaabbbbccddeeff)) {
      // no need to print k. By the time print gets to the value
      // it has already been corrected
      printf("[READER] FAULT DETECTED\n");
      fflush(stdin);
      exit(1);
    }
  }

  printf("[READER] STOP\n");
}


int main(int argc, char const *argv[]) {
  printf("[MAIN] START\n");
  pthread_t reader, writer;

  pthread_create(&writer, NULL, &doWrite, NULL);
  pthread_create(&reader, NULL, &doRead, NULL);

  pthread_join(reader, NULL);
  pthread_join(writer, NULL);

  printf("[MAIN] DONE\n");

  return 0;
}
