iNo = 11 

def Demo () :
    iNo = 51            # Creates SEPERATE NEW varaible in this Demo() local stack named iNo with value 51
    print ("Value of iNo from DEMO ", iNo)

def DemoX () :
    global iNo          # UPDATES GLOBAL Varaible directly.
    iNo = 101
    print ("Value of iNo from DEMOX : ", iNo)

print ("OG iNo : ", iNo)

Demo ()
print ("NEW iNo : ", iNo)       # Well, Doesn't update here as PVM makes seperate varaible in local fun()'s stack

DemoX ()
print ("NEW iNo : ", iNo)

