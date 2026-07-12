print ("Enter Number 1 : ")
iNo1 = input()

print ("Enter Number 2 : ")
iNo2 = input()

#unlike c, cpp, java -> (int)iNo1 --> ERROR : WRONG SYNTAX

iResult = int(iNo1) + int(iNo2)         #TYPE CASTING

print (f"Addition of {iNo1} and {iNo2} : {iResult}")
