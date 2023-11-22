
print('to do list')
tasks=[]
choice='yes'

while choice !='n':
     print("A.add the element")
     print("B.remove the element")
     choice=str(input('do you want to continue a/b/n:'))
     if choice=='n':
          print("quit") 
     if choice=='a':
       task=str(input('enter the string:'))
       tasks.append(task)
     elif choice=='b':
      remove_task = input('enter the string to remove:')
      if remove_task in tasks:
         tasks.remove(remove_task)
         print("task removed")
print(tasks)
    