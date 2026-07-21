import threading

def Display (Test1, Test2, Test3) :   
    print (f"TEST Variable from Thread args : {Test1} {Test2} {Test3}")     

def main () :
    print ("Inside Main () : ", threading.get_ident())
    
    tobj = threading.Thread (target=Display, args=(11,21,51,))    # Super IMP comma , ALWAYS GIVE A COMMA at the END
    tobj.start ()     

if ("__main__" == __name__) :
    main ()
