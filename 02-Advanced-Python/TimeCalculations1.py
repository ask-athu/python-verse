 # To check factorial    4 : 1 * 2 * 3 * 4 (Advantage here is - if amount/size exceeds PVM handles it gracefully)
 # Like int in c has limited size, long (increases its size)
 # # But here no such need.

def main () :
    iValue = int (input ("Enter number to check factorial : "))

    iResult = Factorial (iValue)
    print (f"Factorial of {iValue} is : {iResult}")

def Factorial (iNo) :
    iFact = 1

    for i in range (1, (iNo+1) ) :
        iFact = iFact * i 

    return (iFact)

if ( __name__ == "__main__" ) :
    main ()