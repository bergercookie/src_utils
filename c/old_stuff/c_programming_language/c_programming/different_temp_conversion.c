#include <stdio.h>

#define UPPER 300
#define LOWER 0
#define STEP 20
/* print Fahrenheit-Celsius table */
int main()
{
    int fahr;
    for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
        printf("%3d %6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32));
    printf("\n"); /* Empty line just to seperate the two printing loops*/
    for (fahr = UPPER; fahr >= LOWER; fahr = fahr - STEP) {
        printf("%3d %6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32));
    }
}
