import random

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "1", "2", "3", "4", "5", "6", "!", "@", "#", "$", "%"]
seed = int(input("Enter a seed value: "))
random.seed(seed)
length = int(input("How long of a password do you want? "))

password = ""
for x in range(length):
    char = chars[random.randint(0, len(chars)-1)]
    password += char

print("New Password: " + password)
