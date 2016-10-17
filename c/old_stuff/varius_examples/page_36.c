#include <stdio.h>
#define start 32
#define end 127

/* print out all the printing characters in c */
int main(void)
{
    int n;

    for (n=start; n!=end; ++n) {
    printf("%c=%d\n", n, n);
    }
    return 0;
}
