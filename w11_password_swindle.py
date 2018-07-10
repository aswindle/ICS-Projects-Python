import random
elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
password = ""
random.seed(int(input("Enter seed: ")))
for i in range(0, int(input("How long do you want your password to be? "))):
    password += elements[random.randrange(len(elements))]
print(password)