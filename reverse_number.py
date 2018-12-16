from __future__ import print_function  

n=int(input("Enter the number you want to reverse : "))

rev = 0

while(n>0):
    dig=n%10 #remainder
    rev=rev*10+dig #appending
    n=n//10 #floor division 

print("reverse number is : ",rev)
