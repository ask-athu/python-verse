# Addition and Substraction of 2 numbers via a function & Module 
# L3 CODE

from MyAddition import *

def main () :

    iNumber1 , iNumber2 = getNumbers () 

    print ("Addition : ")
    Display ( Addition (  iNumber1 , iNumber2 ) )

    print ("Substraction : ")
    Display ( Substraction (  iNumber1 , iNumber2 ) )

if ( __name__ == "__main__" ) :
    main ()

