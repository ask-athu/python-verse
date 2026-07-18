def checkEven (iNo) :
    return (iNo % 2 == 0)       # Internally all comparison operators return result in True/False (1/0)

# Reducing code lines : Better practice to covert anu block into lambda
    
def main () :
    iNo = int (input ("Enter a nummber : "))
    bValue = checkEven (iNo) 

    if ( bValue == True) :
        print ("This is an Even Number")
    else :
        print ("This is not an Even Number")

if ("__main__" == __name__) :
    main ()

