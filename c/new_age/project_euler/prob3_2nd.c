#include <stdio.h>

int main()
{
    
    
    int div;
    unsigned long number  = 600851475143;
    printf("\nThe prime factors of %lu are: \n\n",number);
    
    div = 2;
    
    while(number!=0){
        if(number%div!=0)
            div = div + 1;
        else {
            number = number / div;
            printf("%d ",div);
            if(number==1)
                break;
        }
    }
    return 0;
}
