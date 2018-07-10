size = int(input("Enter a size for your array: "))
mylist = []
for i in range(0,size):
    mylist.append(input("Word #" + str(i+1)))
print(mylist)