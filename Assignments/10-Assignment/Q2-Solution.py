def NSum (iNo) :
    
    iSum = 0

    for i in range (1, iNo+1) :
        iSum = iSum + i
        
    print ("Sum of first N Natural Numbers : ", iSum)
    

def main () :
    iValue = int ( input ("Enter a number : "))

    NSum (iValue)

if ( __name__ == "__main__" ) :
    main ()