#include <stdio.h>

int str_len(char *s)
{
    int i;

    for (i=0; *s != '\0'; s++)
        i++;
    return i;
}

int main(void)
{
    char a[] = "Kalimera";
    char *p;

    /* Just Passing a String */
    printf("%d\n", str_len("Hello World"));

    /* Passing an array */
    printf("%d\n", str_len(a));

    /* Passing a pointer */
    p = a + 1;
    printf("%d\n", str_len(p));
    
    return 0;
}
