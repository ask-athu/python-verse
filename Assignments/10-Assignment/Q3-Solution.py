def FactorialX (iNo) :
    
    iFact = 1

    for i in range (1, iNo+1) :
        iFact = iFact * i
        
    print ("Factorial : ", iFact)
    

def main () :
    iValue = int ( input ("Enter a number : "))

    FactorialX (iValue)

if ( __name__ == "__main__" ) :
    main ()