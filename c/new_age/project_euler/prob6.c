/***********************************************
* bcookie, Nikolaos Koukis                     *
*   # Thu Apr 30 23:37:19 CEST 2015, nickkouk  *
*   Project Euler Challenges                   *
*   Problem # 6                                *
************************************************/

// command to run from cmd line: !clear && make && euler_exe

// common includes
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <gsl/gsl_sf_bessel.h>
#include "sup_funs.h"


// definitions
#define arrayMAX 10000

// main algorithm
int main(int argc, const char *argv[])
{
    int result;
    int sumOsquares, squareOsums;

    sumOsquares = sumOsq(0, 100);
    squareOsums = sqOsum(0, 100);
    printf("sumOsquares = %d\n", sumOsquares);
    printf("squareOsums = %d\n", squareOsums);

    result = squareOsums - sumOsquares;
    print_result(result);
    exit(EXIT_SUCCESS); // defined in stdlib.h - use this instead of 0, 1
}
