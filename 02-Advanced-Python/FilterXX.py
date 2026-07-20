# Input dataset -> List -> Filters (Removes Odd Numbers) -> Stores Result Set in Fdata (new list) 

checkEven  = lambda iNo : (iNo % 2 == 0)

def main () :
    Data = [13,12,8,10,11,20]
    
    print ("Present Dataset : ",Data)

    FData = list ( filter (checkEven, Data) )

    print ("Filterd Dataset : ",FData)

if (__name__ == "__main__") :
    main ()
