# Assignment - 02 Q6

def Addition (iNo1, iNo2) :
    return (iNo1 + iNo2)

def Subtraction (iNo1, iNo2) :
    return (iNo1 - iNo2)

def Multiplication (iNo1, iNo2) :
    return (iNo1 * iNo2)

def Division (iNo1, iNo2) :
    return (iNo1 / iNo2)

iValue1 = int (input ("Enter Value 1 : "))
iValue2 = int (input ("Enter Value 2 : "))

print ("Addition : ", Addition(iValue1, iValue2))
print ("Subtraction : ", Subtraction(iValue1, iValue2))
print ("Multiplication : ", Multiplication(iValue1, iValue2))
print ("Division : ", Division(iValue1, iValue2))