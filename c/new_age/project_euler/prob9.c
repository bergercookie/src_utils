/***********************************************
* bcookie, Nikolaos Koukis                     *
*   # Thu Apr 30 23:37:19 CEST 2015, nickkouk  *
*   Project Euler Challenges                   *
*   Problem # 9                                *
************************************************/

// command to run from cmd line: !clear && make && euler_exe

// common includes
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <gsl/gsl_sf_bessel.h>
#include <string.h>
#include "sup_funs.h"

// MACROS

//Adapted from K&R, p.135 of edition 2.
#define len(array) (sizeof((array))/sizeof((array)[0])

// local function declaration
bool exp2sat(unsigned long  a, unsigned long b);

int main(int argc, const char *argv[])
{
    unsigned long a, b, low = 1, high = 800, prod;
    unsigned long a_found = 0, b_found = 0, c_found = 0;
    bool found=false;

    for (a = low; a <= high-1 && found == false; a++) {
        printf("A CHANGED = %lu\n", a);
        for (b = a+1; b <= high; b++) {
            printf("b = %lu\n", b);
            if (exp2sat(a, b)) {
                found = true;
                a_found = a;
                b_found = b;
                c_found = 1000 - a - b;
                break;
            }
        }
    }

    if (found == true) {
        printf("Result found:\n\ta = %lu\n\tb = %lu\n\tc = %lu", a_found, b_found, \
                c_found);

        prod  = a_found*b_found*c_found;
        print_result(prod);
    }
    else 
        printf("Result NOT found.\n");
    exit(EXIT_SUCCESS);
}

bool exp2sat(unsigned long a, unsigned long b) {
    bool it_does;
    int expr = 2000*a + 2000*b - 2*a*b - pow(1000,2);
    if (expr < pow(10,-4) && expr > -pow(10,-4)) {
        it_does = true; 
    }
    else {
        it_does = false;
    }
    return it_does;
}
