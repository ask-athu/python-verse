def DisplayTable (iNo) :
    
    for i in range (1, 11) :
        iResult = iNo * i
        print (f"{iResult}", end = "\t")

def main () :
    iValue = int ( input ("Enter a number : "))

    DisplayTable (iValue)

if ( __name__ == "__main__" ) :
    main ()