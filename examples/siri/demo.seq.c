#include "demo.h"

int x = 0;
int r = 0;

int isr_1() {
  x = 1;
  __VERIFIER_assert(x == 1);
  r = HAL_IO_INPUT(r);
  r = scheduler_reg(r);
  r = HAL_IO_OUTPUT(r);
  Enqueue(0, Q);
  scheduler_deferral(0);
  return 0;
}

int deferral_1() {
  x = 1;
  scheduler_isr(0);
  Dequeue(Q);
  return 0;
}

int isr_2() {
  x = 2;
  scheduler_isr(1);
  return 0;
}

void simulate() {    
  isr[0] = &isr_1;
  isr[1] = &isr_2;
  deferral[0] = &deferral_1;

  int rand = __VERIFIER_nondet() % N;
  pri = prio[rand];
  isr[rand]();
}
