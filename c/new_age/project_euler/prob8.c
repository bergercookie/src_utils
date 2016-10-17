/***********************************************
* bcookie, Nikolaos Koukis                     *
*   # Thu Apr 30 23:37:19 CEST 2015, nickkouk  *
*   Project Euler Challenges                   *
*   Problem # 8                                *
************************************************/

// command to run from cmd line: !clear && make && euler_exe

// common includes
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <gsl/gsl_sf_bessel.h>
#include <string.h>
#include "sup_funs.h"

// local function declaration
unsigned long long cons_prod(char *ptr, int n);

// definitions
char fp_cont[1005];
#define DIGITS 13

int main(int argc, const char *argv[])
{
    unsigned long long result, len, cur_prod, max_prod;
    FILE *fp;
    int i, j, nums[DIGITS];
    char *max_el;

    // nums array initialization
    for (j=0; j< DIGITS; j++)
        nums[j] = 0;

    fp = fopen("supplementary_files/num_prob8", "r");

    // handle potential file failure
    if (fp == NULL) {
        fprintf(stderr, "Can't open input file in.list!\n");
        exit(1);
    }

    fgets(fp_cont, 1001, fp);

    /*printf("the string is the following:\n%s\n", fp_cont);*/
    /*printf("\nthe length of the string is %lu\n", strlen(fp_cont));*/
    /*printf("The product of the 4 first consecutive numbers is: %lu\n", cons_prod(fp_cont, 4));*/

    len = strlen(fp_cont);
    max_prod = 0;

    for (i=0; i<len-DIGITS; i++) {
        cur_prod = cons_prod(&(fp_cont[i]), DIGITS);
        /*printf("cur_prod = %llu\n", cur_prod);*/
        if (cur_prod > max_prod) {
            max_prod = cur_prod;
            printf("max_prod = %llu\n", max_prod);
            getchar();
            // the element referring to the product is going to be the first of
            // the 13
            max_el = &fp_cont[i];
            for (j=0; j < DIGITS; j++) {
                nums[j] = c2d(fp_cont[i+j]);
            }
        }
    }

    for (j=0; j < DIGITS; j++) {
        printf("nums[%d] = %d\n", j, nums[j]);
    }
    result = max_prod;
    print_result(result);
    exit(EXIT_SUCCESS);
}

unsigned long long cons_prod(char *ptr, int n) {
    /* CONS_PROD finds the product of n consecutive numbers starting from the
     * number specified by the ptr pointer */
    int i;
    unsigned long long prod;

    prod =1;
    for (i=0; i<=n-1; i++) {
        prod *= c2d(*(ptr + i));
        /*prod *= c2d(ptr[i]);*/ //alternatively
    }
    return prod;
}
