word = "Batman"
attempt = input("Enter 'Batman' ")
count = 1
while attempt != word:
    count += 1
    attempt = input("Wrong. Enter 'Batman' ")
print("Congratulations. It took you {} tries".format(count))