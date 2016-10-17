#include <stdio.h>

int main(int argc, const char *argv[])
{
    int val = 15;
    int *ptr;
    int **ptr2ptr;

    ptr = &val;
    ptr2ptr = &ptr;

    printf("The value of *ptr is %d\n", *ptr);
    printf("The value of **ptr2ptr is %d\n", **ptr2ptr);
    printf("The initial address of val is %p\n", *ptr2ptr);
    printf("The address of ptr is %p\n", ptr2ptr);
    printf("The address of the ptr again %p\n", &ptr);


   
    return 0;
}
