#include <stdio.h>
// a basic programm that uses switch statements to create predict the month based on interger input from the user

int main()
{
    int month;
    printf(" Enter a number between 1 and 12: ");
    scanf("%d", &month);
    
    switch (month)
    {
    case 1: 
        printf("January");
        break;
    
     case 2: 
        printf("February");
        break;

    case 3: 
        printf("March");
        break;

     case 4: 
        printf("April");
        break;

     case 5: 
        printf("May");
        break;

     case 6: 
        printf("June");
        break;

     case 7: 
        printf("July");
        break;

     case 8: 
        printf("August");
        break;

     case 9: 
        printf("September");
        break;

     case 10: 
        printf("October");
        break;

     case 11: 
        printf("November");
        break;

     case 12: 
        printf("December");
        break;
     
    default:
    printf("Invalid number");
        break;
    }
    return 0;
}
