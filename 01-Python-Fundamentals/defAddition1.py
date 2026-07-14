# Addition of 2 numbers via a function 
# L1 CODE

def main () :

    iValue1 = 0
    print ("Enter Value 1 : ")
    iValue1 = int (input()) 

    iValue2 = 0
    print ("Enter Value 2 : ")
    iValue2 = int (input())

    iResult = 0

    iResult = Addition ( iValue1, iValue2 )

    Display ( iResult )

def Addition ( iNo1, iNo2 ) :
    iAns = 0
    iAns = iNo1 + iNo2
    return (iAns)

def Display ( iAns ) :
    print ("The Addition of two numbers are : ", iAns)

if ( __name__ == "__main__" ) :
    main ()






