import os 

def main () :
    print ("Number of CPU Cores present in my machine : ", os.cpu_count())

if (__name__ == "__main__") :
    main ()