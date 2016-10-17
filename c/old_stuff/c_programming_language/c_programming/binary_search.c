#include <stdio.h>
#define MAX 100
int bin_search(int x, int v[ ], int n)
{
    int low = 0;
    int high = n - 1;
    int i, mid;

    for (i=0; low <= high; i++) {
        mid = (low + high) / 2;
        if (x < v[mid])
            high = mid;
        else if (x > v[mid])
            low = mid + 1;
        else 
            return mid;
    }
    return -1;  /* no match */
}

int main(void)
{
    int i;
    int matrix1[MAX];

    for (i=0; i< MAX; i++)
        matrix1[i] = i * 2;
    
    int x = 34;
    printf("%d\n", bin_search(x, matrix1, MAX));
    
    return 0;
}
