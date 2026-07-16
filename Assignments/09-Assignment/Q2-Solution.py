def CheckGreater (iNo1, iNo2) :

    if (iNo1 > iNo2) :
        print (f"{iNo1} is Greater")
    
    else :
        print (f"{iNo2} is Greater")

def main () :
    
    iValue1 = int (input ("Enter first number  : "))
    iValue2 = int (input ("Enter second number : "))

    CheckGreater (iValue1, iValue2)

if ( __name__ == "__main__" ) :
    main ()