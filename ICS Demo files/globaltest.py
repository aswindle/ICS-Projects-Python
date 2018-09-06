x = 5
y = 7

def do_stuff():
    global x
    x += 10
    global y
    y = 3

do_stuff()
print(x)
print(y)
