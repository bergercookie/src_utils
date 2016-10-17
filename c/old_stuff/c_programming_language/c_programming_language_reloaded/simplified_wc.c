/* INCLUDES */
#include <stdio.h>

/* DEFINES */
#define MAXWORDS 20

void h_histogram(int []); /* Declaring when parameter is array*/
void v_histogram(int []); /* Declaring when parameter is array*/
int max_array(int [], int);

int main(int argc, const char *argv[])
{
    /* Declarations */ 
    int i, c, len;
    int len_array[MAXWORDS];

    /* array 0-ing */
    for (i=0;i<= MAXWORDS;i++)
        len_array[i] = 0;

    c = 0;

    while (c != EOF && (c=getchar()) != EOF) {
        /* counting the chars in each word */
        len=1;
        while (c != ' ' && c != '\n' && c != '\t') {
            if (c == EOF)
                break;
            ++len;
            c = getchar();
        }
        if (len != 1) {
            ++len_array[len - 1];
        }
        else 
            if (c != ' ' || c != '\n' || c != '\t') {
                ++len_array[0];
            }
    }
    printf("\n");
    /*h_histogram(len_array);*/
    v_histogram(len_array);

    return 0;
}

void h_histogram(int lenghts[])
{
    int i, j;

    for (i=1;i<=MAXWORDS;i++) {
        if (lenghts[i] != 0) {
            printf("# of words with %d letters", (i));
            for (j=1;j<=lenghts[i];j++) { /* no lenght starts at 1 */
                printf("-");
                }
            printf("\n");
        }
    }
}

void v_histogram(int lenghts[])
{
    int i, last_pos, noth_more, dashes_counted;
    int zeros_in_row = 0;
    int max_length;

    /* Acual lenght of array */
    last_pos = 0;
    for (i = 1; i<= MAXWORDS; i++) {
        if (lenghts[i] > 0) {
            last_pos = i;
        }
    }

    /* Get the max value from the cells till the last non-zero */
    max_length = max_array(lenghts, last_pos);

    printf("\n\t\t***** WORDS LENGHTS *****\n");
    for (i = 1; i <= last_pos; i++) {
        printf("-%d-\t", i);
    }
    
    printf("\n ");
    dashes_counted = 1;
    while (dashes_counted <= max_length) {
        for (i = 1; i <= last_pos; i++) {
            if (lenghts[i] >= dashes_counted) {
                printf("|");
            }
            printf("\t ");
        }
        printf("\n ");
        ++dashes_counted;
    }
}

int max_array(int array1[], int length)
{
    int the_max =  array1[0];
    int i;


    the_max = 0;
    for (i = 1; i <= length; i++) {
        if (array1[i] > the_max)
            the_max = array1[i];
    }
    return the_max;
}
