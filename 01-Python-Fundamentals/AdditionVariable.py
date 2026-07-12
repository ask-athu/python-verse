iNo1 = 0
iNo2 = 0

print ("Enter Number 1 : ")
#iNo1 = input() --> ERROR 
#                   -> Since python is loosely compiled, so type of variable changes at any time given any condition.
#                   -> so if only input() is used -> makes iNo1 str, overriding the fact that it was initially int

iNo1 = int (input())

print ("Enter Number 2 : ")
iNo2 = int (input())

iResult = iNo1 + iNo2        

print (f"Addition of {iNo1} and {iNo2} : {iResult}")
