# Addition of 2 numbers via a function & Module 
# L3 CODE

from MyAddition import *
# from MyAddition import getNumbers, Display, Addition      --> WORKS

def main () :

    iNumber1 , iNumber2 = getNumbers () 

    Display ( Addition (  iNumber1 , iNumber2 ) )

if ( __name__ == "__main__" ) :
    main ()


# Now no need to write moduleName.function() simply call function 
# Cuz we imported * (all) from our Module : MyAddition




