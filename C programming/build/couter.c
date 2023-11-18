#include <stdio.h>

int main()
{
    int number;

    printf("Enter a number: ");
    scanf("%d", &number);

    int count = 2;
    int sum = 0; 

    while (count < 10)
    {
        printf("The successive sum of %d is: %d\n", count, number + count);
        sum += number + count; 
        count++;
    }

    printf("Final sum: %d\n", sum);
    return 0;
}

 