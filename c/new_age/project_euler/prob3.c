/***********************************************
* bcookie, Nikolaos Koukis                     *
*   # Thu Apr 30 23:37:19 CEST 2015, nickkouk  *
*   Project Euler Challenges                   *
*   Problem # 1                                *
************************************************/
// common includes
#include <stdio.h>
#include <stdbool.h>


// definitions
#define arrayMAX 10000

// function declarations
void  print_result(int);
bool is_prime(int);

int main(int argc, const char *argv[])
{
    /*unsigned long num2check  = 600851475143;*/
    unsigned long num2check  = 100;
    unsigned long rem;
    int i, cur_ind, ar_size;
    int prime_factors[arrayMAX];

    // assemble array of primes
    cur_ind = 0;
    for (i=2; i<= num2check/2 + 1; i++) {
        if (is_prime(i)) {
            prime_factors[cur_ind++] = i;
        }
    }
    ar_size = cur_ind - 1;


    /*print_result(result);*/
}

void print_result(int result) {
    /* PRINT_RESULT: 
     * The purpose of this function is to print the result needed for each one
     * of the levels in the projecteuler challenges. Used to automate the
     * process of printing  */

    printf("\n");
    printf("============================\n");
    printf("---- RESULT COMPUTED -------\n");
    printf("Result = %d\n", result);
    printf("============================\n");
    printf("Exiting... \n");
    fflush(stdout);

    return;
}


bool is_prime(int num) {
    /* IS_PRIME is a function used to determine wether the inputted number num
     * is a prime or not.  Initially designed for problem 3 of projecteuler
     * series */

    int i;
    bool it_is = true;

    for (i = 2; i <= num/2; i++) {
        if (num % i == 0) {
            it_is = false;
        }
    }
    return it_is;
}
