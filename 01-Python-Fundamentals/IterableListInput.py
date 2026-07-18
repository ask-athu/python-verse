def main() :
    Marks = list()  # OOP
    # Marks = []    # SIMPLE WORKING 

    print ("Enter 5 Marks : ")
    for i in range (5) :
        print (f"Enter Marks [{i}] : ")
        no = int (input())
        Marks.append(no)

    print (Marks)

if ( __name__ == "__main__") :
    main ()