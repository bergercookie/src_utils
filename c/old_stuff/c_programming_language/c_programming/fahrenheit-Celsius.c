#include <stdio.h>
/* print Fahrenheit-Celsius table
 * for fahr = 0, 20, ..., 300 */
int main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0; /* lower limit of temperature table */
    upper = 300;
    step = 20;
    fahr = lower;
    printf("Table with Conversions from Fahrenheit to Celsius: \n");
    while (fahr <= upper) {
        celsius = 5. * (fahr - 32.) / 9.;
        printf("%3.0f %60.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
