#include <stdio.h>

enum {MAXPOINTS = 1001, TRUE=1, FALSE=0};

/* struct declarations */
struct point {
    int x;
    int y;
};

struct  rectangle {
    struct point pt1;
    struct point pt2;
};

struct point makepoint(int x, int y);
struct point addpoint(struct point pt1, struct point pt2);
int ptinrect(struct point pt, struct rectangle rect1);

int main(int argc, const char *argv[])
{
    int i;
    struct point *points[10];
    struct point mypoint1, mypoint2, mypoint3;
    struct rectangle my_rect;
    

    mypoint1.x = 0;
    mypoint1.y = 0;
    mypoint2.x = 5;
    mypoint2.y = 5;
    mypoint3.x = 1;
    mypoint3.y = 2;

    my_rect.pt1 = mypoint1;
    my_rect.pt2 = mypoint2;
    /*printf("%d\n", ptinrect(mypoint3, my_rect));*/

    if (ptinrect(mypoint3, my_rect))
        printf("It's in!!\n");
    else
        printf("it's out!!\n");

    return 0;
}

/* Methods regarding the point structure */
struct point makepoint(int x, int y) {
    struct point my_point;
    my_point.x = x;
    my_point.y = y;
    return my_point;
}
struct point addpoint(struct point pt1, struct point pt2) {
    pt1.x += pt2.x;
    pt1.y += pt2.y;

    return pt1;
}


int ptinrect(struct point pt, struct rectangle rect1) {
    int x_in, y_in;
    printf("pt1.y = %d,\tpt.y = %d,\t pt2.y = %d\n", rect1.pt1.y, pt.y, rect1.pt2.y); 

    if ((pt.x >= rect1.pt1.x && pt.x  <= rect1.pt2.x) ||
        (pt.x >= rect1.pt2.x && pt.x  <= rect1.pt1.x)) {
            x_in = TRUE;
    }
    else
        return FALSE;
    if ((pt.y >= rect1.pt1.y && pt.y  <= rect1.pt2.y) ||
        (pt.y >= rect1.pt2.y && pt.y  <= rect1.pt1.y)) {
            y_in = TRUE;
    }
    else
        return FALSE;
    
    return TRUE;
}
