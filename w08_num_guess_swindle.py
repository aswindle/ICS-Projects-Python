change = 256
guess = 512
tries = 1
response = input("Think of a number from 1 to 1000. Type 1 when ready.")
while tries <= 10:
    print("Guess" , tries, ":", guess)
    response = input("Too -high-, too -low-, or -equal-?")
    if response == "high":
        guess = guess - change
    elif response == "low":
        guess = guess + change
    elif response == "equal":
        break
    change = int(change/2)
    tries += 1
print("I win!")