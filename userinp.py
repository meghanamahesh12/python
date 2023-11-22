user_list=[]
user_details = int("input the number of users:")
user_data={}
for i in range(8):
    user_details['name']=input("enter the user name:")
    user_details['age']= input("ENTER THE AGE :")
    user_details ['address'] = input("enter the address: ")
    user_details['contact'] = input("enter the contact :")
user_list.append(user_details)
print(user_details)
print()



