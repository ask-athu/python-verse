# Addition of 2 numbers via a function 
# L2 CODE

def main () :

    iNumber1 , iNumber2 = getNumbers () 

    Display ( Addition (  iNumber1 , iNumber2 ) )

def getNumbers () :

    iValue1 = 0
    print ("Enter Value 1 : ")
    iValue1 = int (input()) 

    iValue2 = 0
    print ("Enter Value 2 : ")
    iValue2 = int (input())

    return (iValue1, iValue2)

def Addition ( iNo1, iNo2 ) :
    iAns = 0
    iAns = iNo1 + iNo2
    return (iAns)

def Display ( iNo3 ) :
    print ("The Addition of two numbers are : ", iNo3)

if ( __name__ == "__main__" ) :
    main ()



