# My own customized filter, map, reduce   

from MyFMRLibrary import filterX, mapX, reduceX

checkEven = lambda iNo : (iNo % 2 == 0)

Increment = lambda iNo : (iNo + 1)

Summation = lambda iNo1, iNo2 : (iNo1 + iNo2)

def main () :
    Data = [13,12,8,10,11,20]
    
    print ("Present Dataset : ",Data)

    FData = list ( filterX (checkEven, Data) )
    print ("Filterd Dataset : ",FData)

    Mdata = list ( mapX (Increment, FData) )
    print ("Mapped Dataset : ",Mdata)

    RData = reduceX (Summation, Mdata)
    print ("Reduced Dataset : ", RData)

if (__name__ == "__main__") :
    main ()