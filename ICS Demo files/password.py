password = "awesome"


user_attempt = input("Enter your password: ")
while user_attempt != password:
    user_attempt = input("Try again")

print("You did it right")
