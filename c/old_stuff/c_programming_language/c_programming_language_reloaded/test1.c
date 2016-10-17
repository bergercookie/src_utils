#include <stdio.h>
void kalimera()
{
    static int i;
    printf("value  of i is: %d\n", i++);
}
int main(int argc, const char *argv[])
{
    int j;
    j = 0;
    while (j++ <= 10) {
        kalimera();
        printf("******\n");
    }
    return 0;
}
