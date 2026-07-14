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

def Substraction ( iNo1, iNo2 ) :
    iAns = 0
    iAns = iNo1 - iNo2
    return (iAns)

def Display ( iNo3 ) :
    print ("The Result of performed operation is : ", iNo3)
