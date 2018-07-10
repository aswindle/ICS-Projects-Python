def split(word):
    half = int(len(word)/2)
    return word[:half] + "|" + word[half:]

def repeat(word):
    return word[0] + word[0] + word + word[-1] + word[-1]

def chop(word):
    return word[1:-1]

def swap(word):
    return word[-1] + word[1:-1] + word[0]

word = input("Enter a word: ")
choice = input("Do you want to split, repeat, chop, or swap? ")

if choice == "split":
    print(split(word))
elif choice == "repeat":
    print(repeat(word))
elif choice == "chop":
    print(chop(word))
else:
    print(swap(word))
