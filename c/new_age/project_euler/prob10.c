/***********************************************
* bcookie, Nikolaos Koukis                     *
*   # Thu Apr 30 23:37:19 CEST 2015, nickkouk  *
*   Project Euler Challenges                   *
*   Problem # 9                                *
************************************************/

// command to run from cmd line: !clear && make && euler_exe

// definitions 
long long last_nnz(unsigned long long *arr, unsigned long long len);

// common includes
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <gsl/gsl_sf_bessel.h>
#include <string.h>
#include "sup_funs.h"

int main(int argc, const char *argv[])
{
/*    unsigned long long lim = 2000000LL;*/
    /*unsigned long long nums2lim[lim];*/

    const unsigned long long lim = 2000000;
    unsigned long long *nums2lim=malloc(lim*sizeof(unsigned long long));
    // initialize nums2lim to 1s
    init_array(nums2lim, lim, 1);
    primes_sieve(nums2lim, lim);

    
    unsigned long long sum = 0;
    for (unsigned long long i=0; i< lim; i++) {
        if (nums2lim[i] != 0) {
            sum += i;
        }
    }
    printf("Sum = %llu\n", sum);

    exit(EXIT_SUCCESS);
}

long long last_nnz(unsigned long long *arr, unsigned long long len) {
    bool found = false;
    long long i, last;

    for (i = len-1; i>0 && found == false; i--) {
        if ( arr[i] != 0 ) {
            found = true;
            last = i;
        }
    }
    printf("last = %llu", last);
    if ( found ) {
        return -1;
    }
    else  {
        return last;
    }

}
