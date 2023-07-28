a=input("enter a list:")
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
    elif i not in c:
        c.append(i)
        print("duplicates valiues are:",c)
