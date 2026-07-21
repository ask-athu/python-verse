import threading
import time

def SumEven (iValue) :
    # Adds up all even number from 0 - iValue
    iEvenSum = 0 
    for i in range (0,iValue,2) :
        iEvenSum = iEvenSum + i

    print (f"The Sum of all Even Numbers upto {iValue} is : {iEvenSum}")

def SumOdd (iValue) :
    # Adds up all odd number from 0 - iValue
    iOddSum = 0 
    for i in range (1,iValue,2) :
        iOddSum = iOddSum + i

    print (f"The Sum of all Odd Numbers upto {iValue} is : {iOddSum}")


def main () :
    iValue = int (input ("Enter a Number : "))

    sTime = time.perf_counter()
    Esum = threading.Thread (target=SumEven, args=(iValue,))

    Osum = threading.Thread (target=SumOdd, args=(iValue,))

    Esum.start()
    Osum.start()
    eTime = time.perf_counter()

    Esum.join() # Makes sure that this threads ends first then rest main() is executed
    Osum.join() # Same This makes running program hold/wait.

    newTime = (eTime - sTime)
    print ("Total Time Taken : ", newTime)


if (__name__ == "__main__") :
    main ()