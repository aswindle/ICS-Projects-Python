
proj9_list = []

num = int(input("Enter how many spaces the list should have: "))
for x in range(num):
    proj9_list += [input("Enter a word: ")]

for x in proj9_list:
    print(x)

if "Batman" in proj9_list:
    print("Congratulations! Batman is a good choice")
elif proj9_list[0] == "Superman" or proj9_list[-1] == "Superman":
    print("You suck")
else:
    print("meh")
