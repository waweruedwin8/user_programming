// this code detects if a number is even or odd
#include <stdio.h>
11
int main()
{
    int number;
    printf(" Enter a whole Number: ");
    scanf("%d", &number);
    
    (number % 2 == 0) ? printf("This is an even number") : printf("This is an odd number");
    return 0;
}