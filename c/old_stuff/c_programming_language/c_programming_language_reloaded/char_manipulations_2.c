#include <stdio.h>

/* The purpose of this program is to pass the inputed text to it's output. 
 * However if the user inputs consecutive spaces then only the first
 * is outputed */

int main(int argc, const char *argv[])
{
    int c = 0;
    int space_already = 0;

    while ((c = getchar()) != EOF) {
        if (c == ' ') {
            if (space_already == 0) {
                putchar(c);
                space_already = 1;
            }
        }
        else {
            space_already = 0; /* Reset the counter*/
            putchar(c);
        }
    }

    return 0;
}
