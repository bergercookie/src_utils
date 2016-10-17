#include <stdio.h>

int main(int argc, const char *argv[])
{
    int c;
    for (c=0; (c = getchar()) != EOF; putchar(c))
        ;
    return 0;
}
