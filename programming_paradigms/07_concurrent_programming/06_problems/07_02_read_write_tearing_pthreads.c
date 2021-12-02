#include <stdio.h>
#include <pthread.h>
#include <unistd.h>


long double k = 0;

// 0x FFFF FFFF FFFF FFFF
// 0x FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF

void * doWrite(void * arg) {
  printf("[WRITER] START\n");

  unsigned char flip = 0;
  while (1) {
    if (flip) {
      k = 0xaaaabbbbccddeeffaaaabbbbccddeeff;
    } else {
      k = 0;
    }

    flip = !flip;
  }

  printf("[WRITER] STOP\n");
}

void * doRead(void * arg) {
  printf("[READER] START\n");

  unsigned char res = 0;
  long double local_k = k;

  while (1) {
    local_k = k;

    if (!(local_k == 0.0 || local_k == 0xaaaabbbbccddeeffaaaabbbbccddeeff)) {
      printf("[READER] FAULT DETECTED %.2Lf \n", local_k);
      fflush(stdin);
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
