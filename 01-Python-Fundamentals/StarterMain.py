def main () :                       # EMPTY Function
    pass
    
if ( __name__ == "__main__" ) :
    main ()                         # We call user-def main() 

"""
“Placing the starter block if __name__ == "__main__": at the end of a Python file does not slow down execution. 
Python parses the all files once, defines all functions, and then runs only the code outside functions. 
The if check is just a single string comparison — negligible in time. Its purpose is structural, not performance: 
    it ensures functions are defined before being called and prevents accidental execution when the file is imported. 

In short, it's a best-practice convention for clean, reusable code, with no measurable impact on speed.”
"""