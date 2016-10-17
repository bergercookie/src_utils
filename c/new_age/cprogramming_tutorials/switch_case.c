#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> // Includes the TRUE boolean operator

/*CAUSE*/
/*The purpose of this module is to learn how to use the CASE statement in C*/

// PROTOTYPES - FUNCTION DECLARATIONS
int parse_input(void);
void decide_input(int num);

// MAIN PROGRAM ROUTINE
int main(int argc, const char *argv[])
{
    int a;

    for (a=parse_input(); a != -1; a=parse_input()) {
        decide_input(a);
    }

    printf("-1 CAUGHT!, Exiting.."); fflush(stdout);
    return 0;
}

// SUPPLEMENTARY FUNCTIONS - DEFINITIONS
void decide_input(int num)
{
    switch (num) {
        case 1:
            printf("Number Inputtted is 1\n");
            break;
        case 2:
            printf("Number Inputtted is 2\n");
            break;
        case 3:
            printf("Number Inputtted is 3\n");
            break;
        default: // ALWAYS include the default case! 
            printf("Number Inputted is above 3...\n");
    }

    return;
}

int parse_input(void)
{
    int num;
    
    printf("Give me a number to compare against a predefined list\n"); fflush(stdout);
    scanf("%d", &num);
    return num;
}
