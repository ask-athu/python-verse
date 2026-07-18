def main () :
    iSize = 0
    Arr = list ()

    print ("Enter the number of elements : ")
    iSize = int (input ())

    for i in range (iSize) :
        print (f"Enter the element at index [{i}] : ")
        iNo = int (input())
        Arr.append(iNo)

    print (Arr)

if ("__main__" == __name__) :
    main ()