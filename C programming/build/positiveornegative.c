#include <stdio.h>
/*a program that outputs if a number is positive, negative or zero*/
int main()
{
    double number;
    
    printf("Enter a number: ");
    scanf("%lf", &number);
    
    if (number >= 0.1)
    {
        printf("The number is positive\n");
    }
    else if (number <= -0.1)
    {
        printf("The number is negative\n ");
    }
    else if (number == 0)
    {
        printf("The number is zero\n");
    }
    return 0;
    
}