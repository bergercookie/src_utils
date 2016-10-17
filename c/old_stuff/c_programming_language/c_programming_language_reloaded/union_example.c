#include <stdio.h>
#include <string.h>

union Data {
    int i;
    float f;
    char str[20];
};

int main(int argc, const char *argv[])
{
    union Data my_data;

    printf("Memory allocated to the union Data of mine: %lu\n", sizeof(union Data));

    my_data.i = 10;
    printf("the int stored in data is:\n%d\n", my_data.i);
    my_data.f = 8.3141527;
    printf("the float stored in data is:\n%3.3f\n", my_data.f);
    strcpy(my_data.str, "kalimera file");
    printf("the string stored in data is:\n%s\n", my_data.str);
    
    return 0;
}
