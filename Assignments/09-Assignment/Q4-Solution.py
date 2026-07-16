def DisplayCube (iValue) :

    iResult = iValue ** 3
    print (f"Cube of {iValue} : {iResult} ")


def main () :
    
    iNo = int (input ("Enter a number  : "))

    DisplayCube (iNo)

if ( __name__ == "__main__" ) :
    main ()