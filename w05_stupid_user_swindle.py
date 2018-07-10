user_text = input("Type 'Batman' ")
tries = 1
while user_text != "Batman":
    user_text = input("You suck. Try again. ")
    tries += 1

print("Congratulations. It took you "+ str(tries) + " tries")
