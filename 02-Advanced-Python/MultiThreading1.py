import threading

def Display () :
    print ("Inside Display () : ", threading.get_ident())

def main () :
    print ("Inside Main () : ", threading.get_ident())

    tobj = threading.Thread (target=Display)    # Assigned task/target to thread ie- Display function()

    tobj.start ()       # Started Thread - Thread's execution starts

if ("__main__" == __name__) :
    main ()

# both values are diff proves this code is multi-threaded.