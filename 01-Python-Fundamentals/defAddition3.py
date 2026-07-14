# Addition of 2 numbers via a function & Module 
# L3 CODE

import MyAddition

def main () :

    iNumber1 , iNumber2 = MyAddition.getNumbers () 

    MyAddition.Display ( MyAddition.Addition (  iNumber1 , iNumber2 ) )

if ( __name__ == "__main__" ) :
    main ()


# 