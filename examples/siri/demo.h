#include "stdio.h"
#include "queue.h"
#include "siri.h"

int DEFERRAL = 0;

int HAL_IO_INPUT(int reg){
    return 10; 
}

int HAL_IO_OUTPUT(int reg){
    return reg;
}

