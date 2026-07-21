import threading

def Display (iTest) :   # Internally : def Display (*iTest) : so iTest aint integer -> its variable no. of args, iterable
    print ("Inside Display () : ", threading.get_ident())
    print (f"TEST Variable from Thread args : {iTest}")     #Catch - Test aint an Int its tuple :)

def main () :
    print ("Inside Main () : ", threading.get_ident())

    # tobj = threading.Thread (target=Display, args=11)   -> here agrs is 11 (int) which aint what is expected as type of args in Thread (it must be an iterable)
    
    tobj = threading.Thread (target=Display, args=(11,))    # Super IMP comma ,
    tobj.start ()       # Started Thread - Thread's execution starts

if ("__main__" == __name__) :
    main ()

