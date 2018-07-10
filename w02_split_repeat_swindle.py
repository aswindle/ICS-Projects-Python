def split(word):
    half = int(len(word)/2)
    return word[:half] + "|" + word[half:]

def repeat(word):
    return word[0] + word[0] + word + word[-1] + word[-1]

print(repeat("hello"))
print(split("blahblah"))
