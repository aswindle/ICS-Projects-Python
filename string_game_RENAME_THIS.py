"""
Your block comment here
"""


# Fill out the code for the 4 functions we need
def chop(word):
    """
    Takes a word and returns the word with its first
    and last characters removed.
    Example: "hello" would return "ell"

    Parameters: word is a string that has at least 2 characters
    Returns: a string
    """
    print("Replace this with your chop code!")


def swap(word):
    """
    Takes a word and returns the word with its first
    and last characters swapped.
    Example: "computer" would return "romputec"

    Parameters: word is a string that has at least 2 characters
    Returns: a string
    """
    print("Replace this with your swap code!")


def split(word):
    """
    Takes a word and returns the word split by '|' at the middle.
    Example: "test" would return "te|st"

    Parameters: word is a string that has an even number of characters
    Returns: a string
    """
    print("Replace this with your split code!")


def repeat(word):
    """
    Takes a word and returns the word with its first
    and last characters repeated three times.
    Example: "computer" would return "cccomputerrr"

    Parameters: word is a string that has at least 2 characters
    Returns: a string
    """
    print("Replace this with your repeat code!")


def main():
    """
    This is where you'll actually use the functions you've written
    above: you'll ask the user for input, determine what they said, and
    then print out the result of running the function
    """

    # Before you worry about asking the user for stuff, I'd recommend
    # testing out your functions on some words and making sure they're
    # working properly. I've included a couple here, but add more!

    print(chop("hello"))
    print(swap("computer"))
    print(split("test"))
    print(repeat("computer"))

    # Once the functions work, finish up the project requirements.
    # I've broken it down into 4 steps:

    # 1. Ask the user to input a word


    # 2. Ask the user to input their choice of function


    # 3. See which operation matches what they typed


    # 4. Print out the result
    chop
    passed = 0
    if chop("hello") == "ell":
        passed += 1
    if chop("computer") == "ompute":
        passed += 1
    if chop("the") == "h":
        passed += 1
    if chop("an") == "":
        passed += 1
    if chop("alexswindle") == "lexswindl":
        passed += 1
    print("Chop: {}/5".format(passed))

    passed = 0
    if swap("hello") == "oellh":
        passed += 1
    if swap("computer") == "romputec":
        passed += 1
    if swap("the") == "eht":
        passed += 1
    if swap("an") == "na":
        passed += 1
    if swap("alexswindle") == "elexswindla":
        passed += 1
    print("Swap: {}/5".format(passed))

    
# This last bit is Python magic. Don't worry about it.
if __name__ == "__main__":
    main()