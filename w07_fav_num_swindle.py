fav = 112
guesses = 1
choice = int(input("Guess a number: "))
while guesses < 10:
    if choice == fav:
        print("You win!")
        break
    elif choice>fav:
        choice = int(input("Too big. Try again. "))
        guesses+=1
    else:
        choice = int(input("Too small. Try again. "))
        guesses+=1
if guesses==10:
    if choice == fav:
        print("You win!")
    else:
        print("You lose.")