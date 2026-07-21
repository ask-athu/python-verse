def filterX (task, dataset) :
    Result = list ()

    for i in dataset :
        element = task (i)       
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