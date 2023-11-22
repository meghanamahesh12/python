# def number_pattern():
#     limit=int(input("Enter thev raw:"))
#     for i in range(1,limit+1):
#         for j in range(i):
#             print(i,end='')
#         print()

def  sum_calculate():
    numbers = [1,2,3,4,5,1,4,5]
 
Sum = sum(numbers)
print(Sum)
 
Sum = sum(numbers, 10)
print(Sum)