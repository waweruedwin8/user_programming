#include <stdio.h>
// explains ternery operators
int main ()
 {23
 int age;
 printf("Enter age: ");
 scanf("%d", &age);
 
 (age >= 18) ? printf("Eligible to drink alcohol") : printf("not eligible to drink alchohol!");
 return 0;
 }