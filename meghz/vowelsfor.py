# a=str(input("enter a word:"))
# count=0
# for i in a:
#     print(i)
#     if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
#        count+=1 
#     print ("No. of vowels:",count)    
  

  #    vowel.py

a=str(input("enter a word:"))
# print(a[::-1])
for i in 'aeiou':
  if i in a:
    print(a[::-1])
  break
else:
  print (" vowels:")    
   
   #reverse print


