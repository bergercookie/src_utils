/* The C Programming Language
 * Example 2 */

#include <stdio.h>
#include <stdlib.h>

int second_main(void)
{
    int fahr;
    int lower, upper, step;
    float celsius;

    lower = 0;
    upper = 300;
    step = 20;

    printf("\n***TEMPERATURE CONVERSION***\n");
    printf("\nCelcius\tFahreneit\n");
    for (fahr = 0;fahr <= upper; fahr = fahr + 20) {
        celsius = 5/9. * (fahr - 32);
        printf("%d\t%6.4f\n", fahr, celsius);
    }
    return(0);
}


int main(void)
{
    second_main();

    printf("\n");
    printf("Program Just exited the second_main function\n");
    /*int fahr;*/
    /*int lower, upper, step;*/
    /*float celsius;*/

    /*lower = 0;*/
    /*upper = 300;*/
    /*step = 20;*/

    /*fahr = lower;*/
    /*printf("\n***TEMPERATURE CONVERSION***\n");*/
    /*printf("\nCelcius\tFahreneit\n");*/
    /*while (fahr <= upper) {*/
        /*celsius = 5/9. * (fahr - 32);*/
        /*printf("%a\t%6.4f\n", fahr, celsius);*/
        /*fahr = fahr + step;*/
    /*}*/
    exit(0);
}
