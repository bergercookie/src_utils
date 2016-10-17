#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char *argv[])
{
    int my_array[100]; // declaring an int array of 100 elements
    char in_string[100];
    char car[50]="car";

    // Enter a phrase
    printf("Give a Word/Phrase:");
    scanf("%s", in_string);

    printf("You inputted the following word/phrase: %s\n", in_string); fflush(stdout);

    printf("\n\n===========================================================\n");
    printf("Address of string array:                   %p\n", in_string);
    printf("Address of the first element of the array: %p\n", &in_string[0]);

    printf("\n\n===========================================================\n");
    printf("Accessing memory of array 7th element: %c\n", in_string[7]);
    printf("Accessing memory of array 99th element: %c\n", in_string[99]);
    printf("Accessing out of array memory: %c\n", in_string[101]);
    return 0;
}

