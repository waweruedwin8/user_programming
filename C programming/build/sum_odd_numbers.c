#include <stdio.h>
// a program that prints the sum of even numbers

int main ()
{
int x;
int sum=0;
for (x=1; x<=100; x+=3)
{
    sum=sum+x;
}
printf(" Sum = %d", sum);
return 0;
}