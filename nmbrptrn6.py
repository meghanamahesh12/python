# limit=int(input("Enter the raw:"))
# num=1
# for i in range(1,limit+1):
#      for j in range(1,i+1):
#           print(num,end='')
#           num+=1
#      print()



limit=int(input("Enter the raw:"))
num=1
for i in range(limit,1):
     for j in range(i+1,limit):
          print(num,end='')
          num+=1
     print()