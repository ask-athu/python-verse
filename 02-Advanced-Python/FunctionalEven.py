checkEven = lambda iNo : (iNo % 2 == 0)

def main () :
    iNo = int (input ("Enter a Number : "))

    if (checkEven(iNo)) :
        print ("It is an Even Number")
    else :
        print ("It is not an Even Number")

if ("__main__" == __name__) :
    main ()