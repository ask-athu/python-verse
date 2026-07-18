def main () :
    iSize = 0
    Arr = list ()

    print ("Enter the number of elements : ")
    iSize = int (input ())

    for i in range (iSize) :
        print (f"Enter the element at index [{i}] : ")
        iNo = int (input())
        Arr.append(iNo)

    Result = Summation (Arr)

    print ("Summation of our List : ", Result)


def Summation (Arr) :
    sum = 0

    for i in Arr :
        sum = sum + i

    return (sum)

if ("__main__" == __name__) :
    main ()