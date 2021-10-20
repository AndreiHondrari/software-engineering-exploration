#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int * array_ptr;
  unsigned int size;
} Array;

#define ARRAY_DEFAULT {.array_ptr=NULL, .size=0}

unsigned char is_divided_by_2(int x) {
  return x % 2 == 0;
}

unsigned char is_divided_by_3(int x) {
  return x % 3 == 0;
}

unsigned char is_over_50(int x) {
  return x > 50;
}

void append_to_array(Array * array, int value) {
  int * new_array_ptr = malloc(sizeof(int) * (array->size + 1));
  int * old_array_ptr = array->array_ptr;

  for (int i = 0; i < array->size; ++i) {
    new_array_ptr[i] = old_array_ptr[i];
  }

  new_array_ptr[array->size] = value;

  array->array_ptr = new_array_ptr;
  array->size += 1;

  free(old_array_ptr);
}

void display_array(Array * array, char * descr) {
  printf("%s: ", descr);

  for (int i = 0; i < array->size; ++i) {
    printf("%d ", array->array_ptr[i]);
  }

  printf("\n");
}

int main(int argc, char const *argv[]) {
  int array_values[] = {
    11, 22, 33, 44, 55, 66, 77, 88, 99,
    110, 120, 130, 140, 150, 160, 170, 180, 190, 200
  };
  int AVSIZE = sizeof(array_values) / sizeof(int);

  Array array1 = ARRAY_DEFAULT;
  for (int i = 0; i < AVSIZE; ++i) {
    append_to_array(&array1, array_values[i]);
  }

  display_array(&array1, "A1");

  Array array2 = ARRAY_DEFAULT;

  // array of function pointers
  unsigned char (*
    criteria_funcs_array[] // our actual array
  )() = {
    &is_divided_by_2, &is_divided_by_3, &is_over_50
  };

  unsigned int CRITERIA_FUNCS_SIZE = (
    sizeof(criteria_funcs_array) / sizeof(unsigned char (*)())
  );

  // iterate over elements in target array
  unsigned char valid = 0;
  for (int i = 0; i < array1.size; ++i) {
    // check value against criteria
    valid = 1;

    for (int j = 0; j < CRITERIA_FUNCS_SIZE; ++j) {
      // get our criteria function
      unsigned char (*criteria_func)() = criteria_funcs_array[j];

      if (criteria_func(array1.array_ptr[i]) == 0) {
        valid = 0;
        break;
      }
    }

    // pass to output array if all criteria passed
    if (valid == 1) {
      append_to_array(&array2, array1.array_ptr[i]);
    }

  }

  display_array(&array2, "A2");

  if (array1.array_ptr != NULL) {
    free(array1.array_ptr);
    array1.size = 0;
  }

  if (array2.array_ptr != NULL) {
    free(array2.array_ptr);
    array2.size = 0;
  }

  return 0;
}
