#include <stdio.h>

/* kalimera is a long unsigned integer. When I decrease it down to -1 it stores trash 
 * inside the  the variable. 
 */
int main(void)
{
    unsigned long kalimera = 5;
    printf("this is the input number: %lu\n", kalimera);
    kalimera -= kalimera + 1;
    printf("this is the input number AGAIN: %lu\n", kalimera);

    return 0;
}
