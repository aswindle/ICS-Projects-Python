def double(word):
    return word + word

def excited(word):
    return "!" + word + "!"

def first(word):
    return word[0]

def main():
    user_word = input("Type a word ")
    user_func = input("Type a function ")

    if user_func == "double":
        print(double(user_word))

    elif user_func == "excited":
        print(excited(user_word))

    elif user_func == "first":
        print(first(user_word))
    else:
        print("Invalid function name")

if __name__ == "__main__":
    main()
