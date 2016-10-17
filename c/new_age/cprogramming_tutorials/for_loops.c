#include <stdio.h>

int main()
{
    int x;
    /* The loop goes while x < 10, and x increases by one every loop*/
    for ( x = 0; x < 10; x++ ) {
        /* Keep in mind that the loop condition checks 
           the conditional statement before it loops again.
           consequently, when x equals 10 the loop breaks.
           x is updated before the condition is checked. */   
        printf( "%d\n", x );

        /*Keep in mind also that the variable is incremented AFTER the code in*/
        /*the loop is run for the first time. */
    }
    printf("Finally OUTSIDE the loop x = %d\n", x);
    getchar();
}
