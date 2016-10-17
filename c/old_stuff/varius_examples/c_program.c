#include <stdio.h>
#include <string.h>

int main(void)
{
    char array1[20] = "Kalimera Ellada";
    char array2[20];
    
    fgets(array2, 20, stdin); /* Input for array2 */

    printf("%lu\n", strlen(array1));
    printf("%s\n", array2);
}
