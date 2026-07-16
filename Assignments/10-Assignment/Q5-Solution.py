def DisplayOdd (iNo) :

    for i in range (1, iNo+1, 2) :
        print (i, end = "\t")
    

def main () :
    iValue = int ( input ("Enter a number : "))

    DisplayOdd (iValue)

if ( __name__ == "__main__" ) :
    main ()