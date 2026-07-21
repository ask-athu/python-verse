import time 

def main () :
    iValue = int (input ("Enter number to check factorial : "))

    start_time = time.time() 

    iResult = Factorial (iValue)
    print (f"Factorial of {iValue} is : {iResult}")

    end_time = time.time()

    print ("Start Time : ", start_time)
    print ("End Time : ", end_time)
    print ("Time taken to complete logic : ", (end_time - start_time), "seconds")

def Factorial (iNo) :
    iFact = 1

    for i in range (1, (iNo+1) ) :
        iFact = iFact * i 

    return (iFact)

if ( __name__ == "__main__" ) :
    main ()