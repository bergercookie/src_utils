/************************************************
 * bcookie, Nikolaos Koukis                     *
 *   # Thu Apr 30 23:37:19 CEST 2015, nickkouk  *
 *   Project Euler                              *
 *   Problem # 1                                *
 ************************************************/

// common includes
#include <stdio.h>

// definitions
#define MAX 1000

// function declarations
void  print_result(int);

int main(int argc, const char *argv[])
{
    // variable declarations
    int num1, num2, i, sum;

    num1 = 3;
    num2 = 5;

    // computation routine
    sum = 0;
    for (i=1; i < MAX; i++) {
        if (i%num1 == 0 || i%num2 == 0) {
            printf("%d is multiple of %d or %d\n", i, num1, num2); fflush(stdout);
            sum += i;
        }
    }
    print_result(sum);
    return 0;
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

