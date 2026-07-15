# Assignment - 07 Q6

def hello () :
    print ("Welcome")

def greet () :
    return hello()

# 1st Case : using () in return
greet ()  

# 2nd Case : wihtout () in return

def greetX () :
    return hello

func = greetX ()
func ()             # prints Welcome

greetX()()          # prints Welcome