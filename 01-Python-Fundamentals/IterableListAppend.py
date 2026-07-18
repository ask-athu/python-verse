def main() :
    Marks = [] 

    Marks.append (11) 
    Marks.append (21)   # PVM kinda uses realloc() internally
    Marks.append (51)

    print (Marks)

if ( __name__ == "__main__") :
    main ()