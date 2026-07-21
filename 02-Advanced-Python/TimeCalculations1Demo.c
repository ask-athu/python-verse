#include <stdio.h>

int Factorial (int iNo) ;

int main (void) 
{
    int iValue = 0 ;

    printf ("Enter a number to check factorial : ");
    scanf ("%d", &iValue) ;

    int iResult = 0 ;

    iResult = Factorial (iValue) ;

    printf ("Factoriral of %d is : %d", iValue, iResult) ;

    return (0) ;
}

int Factorial (int iNo)
{
    int iFact = 1 ;

    for (int i = 1; i<=iNo; ++i)
    {
        iFact = iFact * i ;
    }

    return (iFact) ;

}

/*
C output :
    Enter a number to check factorial : 20
    Factoriral of 20 is : -2102132736           --> Incorrect as value exceeds int size limit

Python output :
    Enter number to check factorial : 20
    Factorial is :  2432902008176640000

C:\Users\vicha\OneDrive\Desktop\Python\SessionWise SRC\Session-06>
*/