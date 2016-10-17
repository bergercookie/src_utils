#include <stdio.h>

/* The purpose of this program is to count 
 * the ammount of tabs, blanks, and */

int main(void) {
int c;

int n_tabs = 0;
int n_blanks = 0;
int n_lines = 0;

while ((c = getchar()) != EOF) {
    if (c == '\t') {
        ++n_tabs; 
    }
    if (c == ' ') {
        ++n_blanks; 
    }
    if (c == '\n') {
        ++n_lines; 
    }
}
printf("*** RESULTS ***\n");
printf("Number of tab characters %d\n", n_tabs);
printf("Number of blank characters %d\n", n_blanks);
printf("Number of newline characters %d\n", n_lines);
}




