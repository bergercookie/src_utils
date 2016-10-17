#include <stdio.h>

int main(void)
{
    int a = 5;
    int b = 6;

    printf("a+(b++):%d\n", a+(b++));
    printf("while a+(++b):%d\n", a + (++b));
}
