#include <stdio.h>

int main(void) {
    int i = 0;

    do {
        printf("%d) timh tou i\n", (i++ + 1));
    }while (i < 10);
    return 0;
}
