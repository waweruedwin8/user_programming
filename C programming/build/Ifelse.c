#include <stdio.h>

int main ()
{
    int age;

    printf("Enter your age: ");
    scanf("%d", &age);

    if (age >= 18)
    {
        printf("you are eligible to vote");
    }

    else
    {
        printf("Sorry you are not eligble to vote");
    }
    return 0;
}