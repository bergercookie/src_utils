#include <stdio.h>
#include <string.h>

int main(int argc, const char *argv[])
{
    char string1[] = "Kalimera";
    int array1[] = {1, 2, 3, 4};
    short int kalimera = 5;

    printf("The size of a char in bytes is: %lu\n", sizeof(char));
    printf("The size of an int in bytes is: %lu\n", sizeof(int));
    printf("The size of a short int in bytes is: %lu\n", sizeof(short int));
    printf("The size of the specific short int in c is %lu\n", sizeof(kalimera));
    printf("The size of a double int in bytes is: %lu\n", sizeof(double));
    printf("The size of the string is %lu\n" , strlen(string1));
    printf("The size of the array1 in memory is %lu\n" , sizeof(array1));
    return 0;
}
