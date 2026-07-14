# Assignment - 03 Q6
from sys import getsizeof

X = 10          # Int
A = 3 + 4j      # Complex

print ("Value in X : ", X)
print ("Data type of X : ", type(X))
print ("Address of X : ", id(X))
print ("Size of X : ",getsizeof(X))

print ("")

print ("Value in A : ", A)
print ("Data type of A : ", type(A))
print ("Address of A : ", id(A))
print ("Size of A : ",getsizeof(A))