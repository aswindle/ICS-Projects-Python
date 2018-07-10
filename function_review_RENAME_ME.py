"""
Fill out your comment block here
"""


# Project 20 is just making sure you can calculate and return the correct values
# from 8 different functions that I've defined. Feel free to use any shortcuts
# you can think of, and you can use some of the functions inside others if you want to
# REMEMBER: Every function should return something, not print something!
# NONE of your functions should include a print() statement


# Functions to write:

# 1: square
# returns the square of the input number.
# Example: 3 -> 9
def square(num):



# 2: cube
# returns the cube of the input number
# Example: 3 -> 27
def cube(num):



# 3: double_string
# returns a doubled version of the input string
# Example: "the" -> "thethe"
def double_string(text):



# 4: list_string
# returns a list that contains all of the characters of an input string
# Example: "hello" -> ['h', 'e', 'l', 'l', 'o']
def list_string(text):



# 5: sum
# returns the sum from 1 to the input number n
# Example: sum(5) -> 15, which is 1+2+3+4+5
def sum(n):



# 6: sum2
# returns the sum of the values stored inside a list
# Example: sum([1, 3, 5]) -> 9
def sum2(array):


# 7: average
# returns the average of the values stored inside a list
# Example: average([1, 3, 5]) -> 3.0
def average(array):



# 8: factorial
# returns n!, which is 1*2*3*...*n
# Example: factorial(4) -> 24. Hint: be careful with the bounds in your loop
def factorial(n):

# Grading Code:
x = square(3) + square(4)
print("25: " + str(x))

x = cube(2) + cube(3)
print("35: " + str(x))

x = double_string("Batman")
print("BatmanBatman: " + x)

x = list_string("Batman")
print(x)

x = sum(5) + sum(3)
print("21: " + str(x))

x = sum2([1, 3, 8])
print("12: " + str(x))

x = average([2, 6, 10])
print("6: " + str(x))

x = factorial(4) + factorial(3)
print("30: " + str(x))

