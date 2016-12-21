#include "queue.h"

int pri = 0;
int prio[2] = {1, 2};
int N = 2;
int REG = 10;
int * (*isr[2])();
int * (*deferral[1])();

void __VERIFIER_assert(int cond) { if (!(cond)) { ERROR: __VERIFIER_error(); } return; }

void scheduler_isr(int id) {
  int p = pri;
  for(int i = 0; i < 2; i++) {
    if(__VERIFIER_nondet() && i != id && prio[i] > pri) {
      pri = prio[i];
      isr[i]();
    }
  }
  pri = p;  
}

void scheduler_deferral(int id) {   
  if(id != Head(Q))
    return;
  else
    deferral[id]();
}

int scheduler_reg(int reg) {   
  if(__VERIFIER_nondet())
    return -1;
  else
    return reg;
}
