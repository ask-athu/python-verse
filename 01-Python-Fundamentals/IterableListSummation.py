def main () :
    Data1 = [10, 11, 21, 51]

    result = ListSummation(Data1)

    print ("Summation of List is : ", result)

def ListSummation ( Data1 ) :
    sum = 0
    for i in Data1 :
        sum = sum + i

    return (sum)

if ("__main__" == __name__) :
    main ()