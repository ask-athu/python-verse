import threading

def Display () :
    print ("Inside Display () : ", threading.get_ident())

def main () :
    print ("Inside Main () : ", threading.get_ident())

    Display ()

if ("__main__" == __name__) :
    main ()

# Both values are same proves this code is single-threaded.
# get_ident() returns Thread Number (ie- Tid)