# My own customized filter, map, reduce   

checkEven = lambda iNo : (iNo % 2 == 0)

Increment = lambda iNo : (iNo + 1)

Summation = lambda iNo1, iNo2 : (iNo1 + iNo2)

def filterX (task, dataset) :
    Result = list ()

    for i in dataset :
        element = task (i)       # call : checkEven (iNo)
        if (element == True) :
            Result.append(i)

    return Result

def mapX (task, dataset) :
    Result = list ()

    for i in dataset :
        element = task (i)
        Result.append(element)

    return Result

def reduceX (task, dataset) :

    Result = 0

    for i in dataset :
        Result = task (Result, i)
    
    return Result

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


# NOTE : 1st Parameter of filter function (here checkEven) MUST ALWAYS return bool