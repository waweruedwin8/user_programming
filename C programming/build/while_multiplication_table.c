#include<stdio.h>
// a program that impliments a multiplication  table that multplies numbers backward using a while loop 

int main()
{
    int count = 10;
    int number;
    int product;

    printf(" Enter a number to be  multiplied:  ");
    scanf("%d", &number);

    while (count >= 1)
    {
        int product = number * count ;9
        printf("%d * %d = %d\n",number,count ,product);
        count--;
    }
    return 0;
}