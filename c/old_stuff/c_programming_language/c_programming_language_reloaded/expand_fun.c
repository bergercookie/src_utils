
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void expand(char s1[], char s2[]);

enum constants { MAXCHARS = 1000 };

int main(int argc, const char *argv[])
{
    char string1[100], string2[MAXCHARS];
    int i;

    // matrix initialization
    for (i=0; i <= 100; i++)
        string1[i] = 0;
    for (i=0; i <= MAXCHARS; i++)
        string2[i] = 0;

    printf("Give something to expand:\n");
    scanf("%s", string1);

    printf("Expansion Coming up\n");
    expand(string1, string2);
    printf("\nExpanded String is:\n%s\n", string2);
    return 0;
}

void expand(char s1[], char s2[])
{
    /* s1 should be something like 
     * a-z or a-b-c or a-z0-9
     * s2 should be the char array expanded */

    int i, j, count, begin, end, loops_num;


    loops_num = 0;
    begin = s1[0];
    if (s1[1] == '-') {
        end = s1[2];
    }

    /*printf("begin = %d\nend = %d", begin, end);*/
    count = 0; // variable to get the current position of the end matrix
    for (i=0; i<= strlen(s1); i++) {
        if (s1[i] == '-') { 
            for (j = s1[i-1]; j <= s1[i+1]; j++, count++) {
                s2[count] = j; 
            }
        }
        /*printf("Letter = %c\n", s2[i-'a']);*/
    }
    return;
}
