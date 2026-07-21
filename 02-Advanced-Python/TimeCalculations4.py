import time 

def main () :
    iValue = int (input ("Enter number to check factorial : "))

    start_time = time.perf_counter()   # Better method than time() to calculate time.   USED IN TIME COMPLEXITY

    iResult = Factorial (iValue)
    print (f"Factorial of {iValue} is : {iResult}")

    end_time = time.perf_counter()

    print ("Start Time : ", start_time)
    print ("End Time : ", end_time)
    print (f"Time taken to complete logic : {end_time - start_time:.5f} seconds") 

def Factorial (iNo) :
    iFact = 1

    for i in range (1, (iNo+1) ) :
        iFact = iFact * i 

    return (iFact)

if ( __name__ == "__main__" ) :
    main ()