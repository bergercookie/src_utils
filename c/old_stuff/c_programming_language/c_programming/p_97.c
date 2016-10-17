#include <stdio.h>

int main(void)
{
    int  *pa;
    int array1[10];

    /* output of sizeof
     * is this
     * shit over here
     */
    printf("%lu\n", sizeof(pa));
    
    int i;

    /* Initialization of array1 */
    for (i=0; i < 10; i++) {
        array1[i] = i + 2;
    }
    
    pa = &array1[0];   
    /* I can also say pa = array1 
     * because array1 returns the address of its first element!
     */
    /* Values of array1 */
    for (i = 0; i < 10; i++) {
        printf("%d\n", *(pa + i));
    }
    return 0;
}

