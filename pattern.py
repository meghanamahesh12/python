#pattern square
#--------------

# limit=int(input("Enter the row:"))
# for i in range(0,limit):
#     print("*"*4)

#pattern triangle
# ----------------
# limit=int(input("Enter the row:"))
# for i in range(1,limit):
#    #for e in range(0,i+1):
#      print("*"*i)





limit=int(input("Enter the row:"))
for i in range(1,limit):
   #for e in range(0,i+1):
     print("*"*i)

#pattern invert triangle
#-----------------------
limit=int(input("Enter the row:"))
for i in range(0,limit+1):
     s=limit-i
     print(" "*s,"*"*i)

#pattern
#-------
# limit=int(input("Enter the row:"))
# for i in range(0,limit-1):
#      print("*"*i," "*s)
#      s=i-limit