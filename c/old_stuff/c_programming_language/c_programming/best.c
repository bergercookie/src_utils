#include <stdio.h>
#include <stdlib.h>
void strcopy(char *p, char *q);

int main(void)
{
    char *first = "kalimera";
    char *second = malloc(sizeof(first));
    strcopy(first, second);
    printf("%s\n", second);

    free(second);
    return 0;
}

/* function for copying a string into another */
void strcopy(char *p,char *q)
{
   while ((*q++ = *p++) != '\0')
        ;;
}
