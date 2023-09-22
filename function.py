def pattern():


for i in range(1,limit+1):
    for j in range(i,-1,0):
          if i!=0 and j==i:
               print("1",end='')
          else:
               print("2",end='')
    print()