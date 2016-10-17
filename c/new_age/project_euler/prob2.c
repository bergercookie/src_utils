/***********************************************
* bcookie, Nikolaos Koukis                     *
*   # Thu Apr 30 23:37:19 CEST 2015, nickkouk  *
*   Project Euler Challenges                   *
*   Problem # 1                                *
************************************************/
// common includes
#include <stdio.h>

// definitions
#define MAX 4e6

// function declarations
void  print_result(int);

int main(int argc, const char *argv[])
{
    // variable declarations
    int num1, num2, num3, sum;

    // first 2 fib numbers
    num1 = 1;
    num2 = 2;

    // computation routine
    sum = 2; //2 is a even number as well..
    do {
        num3 = num1 + num2;
        if (num3 % 2 == 0) {
            printf("%d is an even Fibonacci number\n", num3);
            sum += num3;
        }
        num1 = num2;
        num2 = num3;
    } while (num3 <= MAX);

    // postprocessing
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


