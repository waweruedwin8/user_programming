#include<stdio.h>
// a simple program that inputs int and either uses +,-,/, operators to give a result
 
 int main()
 {
    int a;
    int b;
    char sign;
    int result;

    printf("Enter the first number: ");
    scanf("%d",&a);

    printf("Enter your prefferd  mathematical sign: ");
    scanf(" %c",&sign);

    printf("Enter the second number: ");
    scanf("%d,",&b);

if (sign=='+')
{
    result = a + b;
    printf("The sum of %d and %d is:  %d \n",a,b,result);
}
else if (sign == '-')
{
    result = a - b;
    printf("The subtraction of %d and %d is:  %d \n",a,b,result);
}
else if (sign == '*')
{
    result = a * b;
    printf("The multiple of %d and %d is:  %d \n",a,b,result);
}
else if (sign=='/')
{
    result = a/b;
    printf("The division of %d and %d is %d \n",a,b,result);
}
 else
 { 
    printf("The mathematical sign you entered is invalid!");
 }
    return 0;
}
