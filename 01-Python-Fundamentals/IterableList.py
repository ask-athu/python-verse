lData1 = [1,2,3,4,"One"]
print ("Displaying List 1 : ", lData1)

lData1 = [5,6,7,8,"Two"]        # MODIFYING VALUES 

print ("Enter your new List : ")
lData2 = list(input()) 

lData3 = [10,10,10.9,"Four"]    # Duplicates values inserted.

# BASIC
print ("Displaying List 1 : ",lData1)

# SIMPLEST
for i in lData2 : 
    print (i) 

# OG For loop 
for x in range (len(lData3)) :      #len(lData4) : length of lData4 -> 4
    print (lData3[x])