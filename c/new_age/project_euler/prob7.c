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
#define num_lim 10001 //number of primes to find

// main algorithm
int main(int argc, const char *argv[])
{
    int count, i;
    unsigned long result;

    count = 1; //2 is a prime
    for (i=3; count<num_lim; i+=2) {
        if (is_prime(i)) {
            count++;
            printf("count = %d; i = %d\n", count, i);
        }
    }
    result = i - 2;

    print_result(result);
    exit(EXIT_SUCCESS);
}
