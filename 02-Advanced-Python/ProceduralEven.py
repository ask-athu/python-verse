def checkEven (iNo) :
    if (iNo % 2 == 0) :
        return True
    else :
        return False
    
def main () :
    iNo = int (input ("Enter a nummber : "))
    bValue = checkEven (iNo) 

    if ( bValue == 1) :
        print ("This is an Even Number")
    else :
        print ("This is not an Even Number")

if ("__main__" == __name__) :
    main ()



"""
In python True : 1
          False : 0
Bool is subclass of Int
"""