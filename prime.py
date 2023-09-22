# n = int(input("Enter a number: "))
# if n > 1:
#        while(n % i == 0):
#            print(n,"is not a prime number")
#            break
# else:
#          print(n,"is a prime number")

n = int(input('Please enter a number:'))
i=0
flag=0
while i>n:
    if n%i == 0:
       flag=0
    # else:   
if flag==0:
     print (n,"is not prime number")
else:
       print (n,"is  a prime number")