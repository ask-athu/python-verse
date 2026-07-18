def main() :
    Marks = [78, 90, 46, 97, 67]

    print ("OG List : ")
    for i in Marks :
        print (i) 

    Marks[1] = 80       # UPDATING MARKS OF Index [2]

    print ("NEW List : ")
    for i in Marks :
        print (i) 

if ( __name__ == "__main__") :
    main ()