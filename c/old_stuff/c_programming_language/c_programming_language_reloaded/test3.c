#include <stdio.h>

int main(int argc, const char *argv[])
{
    int x[10] = {100, 200, 300, 400, 500, 600, 700, 800 , 900, 1000};
    int ptr1, ptr2;
    int i, j;

    printf("x[9] = %d, *(x+9) = %d\n", x[9], x[9]);
    printf("&(x[10] = %d, x + 10 = %d\n", x[9], x[9]);

    // for any pointer or array -> x[10] == *(x+10)
    // it is possible to substract an integer from a pointer 
    // it is possible to find the integer difference between two pointers
    return 0;
}
