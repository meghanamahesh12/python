# a=int(input("enter a number :"))
# i=0
# sumo=0
# sume=0
# while i<=a:
#    if a%2==0:
#     sumo=sumo+a
#     print("sum of odd numbers",sumo)
#    else: 
#     sume=sume+a 
#     print("sum of even numbers",sume)
# i+=1    21






a=int(input("enter a number :"))
sum = 0
i = 0
while i<=a:
   if i%2==0:
    print("sum of even numbers",sum)
   else: 
      print("sum of odd numbers",sum)   
sum+=i
i+=1