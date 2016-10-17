#include <stdio.h>
#include <stdlib.h>
#define MAXPOINTS 1000

struct point {
    int x;
    int y;
};

struct point *makepoint(int x, int y);

int main(int argc, const char *argv[])
{
    int i;
    int number1 = 5, number2 = 10;
    struct point *points[10];
    
    for (i=0; i< MAXPOINTS; i++) {
        points[i]  = (makepoint(number1, number2));
    }
}

struct point *makepoint(int x, int y) {
    struct point *my_point = malloc(sizeof(struct point));
    my_point->x = x;
    my_point->y = y;
    return my_point;
}
