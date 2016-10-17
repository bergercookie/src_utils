/***********************************************
* bcookie, Nikolaos Koukis                     *
*   # Thu Apr 30 23:37:19 CEST 2015, nickkouk  *
*   Project Euler Challenges                   *
*   Problem # 5                                *
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

    int i, j, result;
    int loop_start = 20; 
    bool found = false;

    // main routine to determine the largest evenly-divisible num
    for (i=20; found == false; i+= 20) {
        // compare against the primes list
        printf("i = %d\n", i);
        for (j=2; j<= 20; j++) {
            if (i % j != 0) {
                break;
            }
        }
        if ((j == 21) && (i%20 == 0)){
            // has exited the loop normally - get that number
            found = true;
            result = i;
        }
    }
    print_result(result);
    exit(EXIT_SUCCESS); // defined in stdlib.h - use this instead of 0, 1
}
