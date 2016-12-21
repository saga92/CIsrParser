#include "demo.h"

int x = 0;
int r = 0;

int isr_1() {
  x = 1;
  int z = 3; 
  r = HAL_IO_INPUT(r);
  r = HAL_IO_OUTPUT(r);
  return 0;
}

int deferral_1() {
  x = 1;
  return 0;
}

int isr_2() {
  x = 2;
  return 0;
}

