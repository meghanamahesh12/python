# list=[]
# user_num=int(input("enter the number of user:"))
# for i in range(user_num):
#  details={}
#  details['name']=input("enter the user name:")
# details['age']= input("enter the age :")
# details['contact'] = input("enter the contact:")
# details['balance'] = input("enter the amount:")
# list.append(details)
# print("\ninformation")
# for details in list:
#  print("name:",details["name"])
#  print("age:",details["age"])
#  print("contact",details["contact"])
#  print("balance",details["amount"])
#  print()
#  details.update({"balance":"amount"})
# print(list)









# banks=[]
# user_num=int(input("enter the number of user:"))
# for i in range(user_num):
#  accounts={}
#  balance=0
# choice="yes/no"
# while choice !='D':
#      print("A.enter the account deatils")
#      print("B.deposit")
#      print("C.withdraw")
#      print("D.quit")
# choice=input("enter your choice")
# if choice==1:     
#      if choice=='A':
#        bank=str(input('enter the details:'))
#        banks.append(bank)
#      elif choice=='B':
#        banks= input('enter the deposit:')
#      elif choice=='C':
#         banks=input ("withdraw")
# print(banks)     






list=[]
accounts={}
while True:
   print("1.enter the user:","2.account details","3.deposit","4.withdraw","5.quit")
   choice=input("enter your choice:")
   if choice=="1":
    name=input("enter the name:")
    branch=input("enter the branch:")
    balance=0
    accounts["name"]=name
    accounts["branch"]=branch
    accounts["balance"]=balance
    list.append(accounts.copy())
    print(list)

   elif choice=="2":
    for accounts in list:
     print("name:",accounts["name"])
     print("branch",accounts["branch"])
     print("balance",accounts["balance"])

   elif choice=="3":
    print(balance)
    user=input("enter username:")
    deposit=int(input("enter the amount to deposit:"))
    for accounts in list:
     if accounts["name"]==user:
        accounts["balance"]+=deposit
        print("amount deposited suucessfully!..current bank balance=",accounts["balance"]) 


   elif choice=="4":
     print(balance)
     user=input("enter username:")
     amount=int(input("enter the amount withdraw:"))
     for accounts in list:
      
      if accounts["name"]==user:
       if accounts["balance"]<=amount:
             print("insufficient")        

      else:
          accounts["balance"]-=amount
          print("amount withdraw suucessfully!..new bank balance:",accounts["balance"]) 
   elif choice=="5" :
     print("completed")
     break
   else:
     print("invalid")