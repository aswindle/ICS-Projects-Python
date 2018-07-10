"""
Inspired by Howard Beck copyright 2017
"""
from test.test_wsgiref import hello_app

word = input("Enter a word: ")
binary = ' '.join(format(ord(x), 'b') for x in word)
result = ""
for num in binary:
    if num == "1":
        result += "beep "
    elif num == "0":
        result += "boop "
    else:
        result += "  "
print(result)

print hello

