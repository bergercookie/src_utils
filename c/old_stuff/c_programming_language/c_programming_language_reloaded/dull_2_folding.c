
/* The purpose of this program is to fold inputted lines to the n-th column.
 * Lines that are larger than that limit should continue on the 80 line */

#include <stdio.h>
#include <stdlib.h>

enum constants {MAXLINE = 1000};

int main(int argc, const char *argv[])
{
    int i, c, real_len;
    int big_line[MAXLINE];
    int line_lim;
    int how_many =0;

    if (argc == 1) {
        printf("You need to give the line limit\nExiting ..\n");
        exit(1);
    }
    else if (argc == 2)  {
        line_lim = atoi(argv[1]);
        printf("The Line limit is set: %d\n", line_lim); /* parses it as a char!!! */
    }
    else {
        printf("Too many input values, argc = %d\nExiting ..\n", argc);
        exit(1);
    }

    for (i=0; ((c=getchar()) != EOF && c != '\n'); big_line[i++]  = c);
    real_len = i-1;

    printf("\n\t\t\t***Printing with fold limitation***\n\n");
    for (i=0; i <= real_len; i++) {
        if (how_many <= line_lim) {
            putchar(big_line[i]);
            how_many++;
        }
        else if (big_line[i] == '\t' || big_line[i] == ' ') {
            ;

        }
        else {
            putchar('\n');
            how_many = 1;
            putchar(big_line[i]);
        }
    }
    printf("\n");

}
