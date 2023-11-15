#include <stdio.h>
#include <stdarg.h>

// function prototype

int add(int n, ...);

int main ()
{
    printf("addition 1 = %d\n", add (7, 5,6,9,3,4,7,3))
    return 0;
}

int add (int n, ... ) // variadic function
{
    va_list list;
    va_start(list, n);

    int i, sum = 0;
    for (i = 0; i < n; i++)
    sum += va_arg(list, int);

    va_end(list)
    return sum;
}