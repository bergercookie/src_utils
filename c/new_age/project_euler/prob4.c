/***********************************************
* bcookie, Nikolaos Koukis                     *
*   # Thu Apr 30 23:37:19 CEST 2015, nickkouk  *
*   Project Euler Challenges                   *
*   Problem # 4                                *
************************************************/

// command to run from cmd line: !clear && make && euler_exe

// common includes
#include <stdio.h>
#include <stdbool.h>
#include "stdlib.h"
#include <gsl/gsl_sf_bessel.h>
#include "sup_funs.h"


// definitions
#define arrayMAX 10000

// main algorithm
int main(int argc, const char *argv[])
{
    int i, j, current;
    bool found;
    int *result_ar[3];
    int the_max = 0;

    /*printf("is_palindrome(6006) = %d, is_palindrome(6024) = %d\n", is_palindrome(num1), is_palindrome(num2));*/


    // opposite traversing to find it faster
    for (i=999; i>=100;  i--) {
        for (j=999; j>=100; j--) {
            printf("i: %d\tj: %d\n", i, j);

            if (is_palindrome(i*j)) {
                /*found = true;*/

                current = i*j;
                if (the_max < current) {

                    the_max = current;
                    // store the results into the array
                    (*result_ar)[0] = i;
                    (*result_ar)[1] = j;
                    (*result_ar)[2] = i*j;
                    /*break;*/
                }
            }
        }
        /*if (found)*/
            /*break;*/
    }
    print_result((*result_ar)[2]);
    exit(EXIT_SUCCESS); // defined in stdlib.h - use this instead of 0, 1
}
