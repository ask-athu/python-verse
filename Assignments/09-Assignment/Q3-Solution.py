def DisplaySqaure (iValue) :

    iResult = iValue ** 2
    print (f"Square of {iValue} : {iResult} ")


def main () :
    
    iNo = int (input ("Enter a number  : "))

    DisplaySqaure (iNo)


if ( __name__ == "__main__" ) :
    main ()