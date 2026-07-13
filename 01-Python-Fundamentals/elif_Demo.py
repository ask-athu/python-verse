print ("Welcome to CITY PARK !")

print ("Confirm your Age to calculate fare : ")
iAge = int (input())

if (iAge == 0) :
    print ("INVALID AGE")

elif (iAge <= 5) :
    print ("FREE! $0")

elif (iAge > 5 and iAge < 16) :
    print ("FARE : $300")

elif (iAge > 16 and iAge < 50) :
    print ("FARE : $700")

else :
    print ("FARE : $500")

