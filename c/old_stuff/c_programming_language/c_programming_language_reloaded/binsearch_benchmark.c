#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int binsearch_book(int [], int, int);
int binsearch_mine(int [], int, int);

enum constants {MAXLEN = 10000000};

int main(int argc, const char *argv[])
{
    int number, length;
    int i;
    const char * option;
    int position;
    int list1[MAXLEN];


    /* Arguement Parsing */
    if (argc < 4) {
        printf("Need to input which binsearch function to run (book / mine)");
        printf("as well as lenght of sorted array and the number to match\nExiting ..\n");
        exit(1);
    }
    else if (argc > 4) {
        printf("Too many arguements given!\nExiting ..");
        exit(1);
    }
    else {
        option = argv[1];
        length = atoi(argv[2]);
        number = atoi(argv[3]);
        /* Checking the parameter input */
        printf("Number = %d\nOption = %s\nlenght = %d\n", number, option, length);
    }

    for (i=0; i <= length - 1; list1[i] = 10 * i)
        i++;

    /* Finding the position */
    position = (!strcmp(argv[1], "book")) ? binsearch_book(list1, number, length) : binsearch_mine(list1, number, length);
    printf("*Position Found!* ----> %d\n", position);
    printf("Exiting ..\n");

    return 0;
}

int binsearch_book(int v[], int x, int n)
{
    int low, high, mid;
    printf("Executing the *book* search\n");

    low = 0;
    high = n - 1;
    while (low <= high) {
        mid = (low + high) / 2;
        if (x < v[mid] )
            high = mid - 1;
        else if (x > v[mid])
            low = mid + 1;
        else /* found match */
                return mid;
    }
    return -1; /* no match */
}

int binsearch_mine(int v[], int x, int n)
{
    int low, high, mid;

    printf("Executing my search\n");
    low = 0;
    high = n - 1;
    mid = (high + low ) / 2;
    while (low <= high && x != v[mid]) {
        if (x < v[mid]) 
            high = mid - 1;
        else 
            low = mid + 1;
        mid = (high + low ) / 2;
    }
    if (low > high)
        return -1; /* no match */
    else 
        return mid;
}
