#include <stdio.h>
#include <stdlib.h>


void swap(int *a, int *b);

int main(void)
{
    /*
    int *a = malloc(sizeof(int));
    int *b = malloc(sizeof(int));

    printf("%s\n", "Give a");
    scanf("%d", a);
    printf("%s\n", "Give b");
    scanf("%d", b);
    */
    int *a;
    int *b;
    int dummy[10];
    int i;

    for (i=0; i<10; i++)
        dummy[i] = i + 5;
    b = &dummy[0] + 1;
    a = dummy + 2;
    swap(a, b);
    printf("a:%d,b:%d\n", *a, *b);

    /*free(a, b);*/
    return 0;
}

void swap(int *a, int *b)
{
    int temp;

    temp =  *a;
    *a = *b;
    *b = temp;
}
