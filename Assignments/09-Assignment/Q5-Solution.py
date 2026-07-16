def checkDivisiblity (iValue) :

    if ( (iValue % 5 == 0) and (iValue % 3 == 0) ) :
        print ("Divisible by 3 and 5")
    
    else :
        print ("Not divisible by 3 and 5")

def main () :
    
    iNo = int ( input ("Enter a number : "))

    checkDivisiblity (iNo)

if ( __name__ == "__main__" ) :
    main ()