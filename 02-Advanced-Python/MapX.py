# MapX -> bcuz there might exist an inbuild module with name Filter.py
# Input dataset[] -> List -> Filters (Removes Odd Numbers) -> Stores Result Set in Fdata[] (new list) -> Map FData (Add 1) -> Stores in Mdata[]

def checkEven (iNo) :
    return (iNo % 2 == 0)

def Increment (iNo) :
    return (iNo + 1)

def main () :
    Data = [13,12,8,10,11,20]
    
    print ("Present Dataset : ",Data)

    FData = list ( filter (checkEven, Data) )
    print ("Filterd Dataset : ",FData)

    Mdata = list ( map (Increment, FData) )
    print ("Mapped Dataset : ",Mdata)

if (__name__ == "__main__") :
    main ()


# NOTE : 1st Parameter of filter function (here checkEven) MUST ALWAYS return bool