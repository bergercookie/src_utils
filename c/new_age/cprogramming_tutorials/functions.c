#include <stdlib.h>
#include <stdio.h>

// PROTOTYPES - FUNCTION DECLARATIONS
double mult(double x, double y);
double div2(double x, double y);

// MAIN PROGRAM ROUTINE
int main()
{
    // DECLARATIONS
    double mult_out, div2_out;
    double num1, num2;

    // INPUTS
    printf("Give 2 numbers to work with:\n"); fflush(stdout);
    scanf("%lg %lg", &num1, &num2);

    // COMPUTING
    mult_out = mult(num1, num2);
    div2_out = div2(num1, num2);

    // PRINTING THE RESULTS
    printf("Multiplication outcome: %g\n", mult_out);
    printf("Division outcome: %g\n", div2_out);
}

// SUPPLEMENTARY FUNCTIONS - DEFINITIONS
double mult(double x, double y)
{
    double outcome;
    outcome = x * y;

    return outcome;
}

double div2(double x, double y)
{
    double outcome;
    outcome = x / y;

    return outcome;
}
