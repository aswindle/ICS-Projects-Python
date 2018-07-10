def print_num(num):
    for i in range(1,num+1):
        print(i)

def num_back(num):
    for i in range(0,num):
        print(num-i)

def add(num):
    total = 0
    for i in range(1,num+1):
        sum += i
    print(total)
        
user_num = int(input("Type a number: "))
choice = input("Choose an operator: print, back, or add ")
if choice=="print":
    print_num(user_num)
elif choice =="back":
    num_back(user_num)
else:
    add(user_num)
