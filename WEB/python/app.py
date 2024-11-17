# variables

# students_count = 100
# rating = 4.99
# is_published = False
# course_name = 'Python'


# x, y = 1, 2

# x, y = 1


# Dynamic Typing

# students_count = 1000
# print(type(students_count))


# Type Annotation

# age: int = 17
# age = "Python"
# print(age)


# Mutable and immuble types
# x = [1, 2, 3]
# print(id(x))

# x.append(4, 5)
# print(id(x))


# Srings

# course = "Python Programming"

# print(len(course))
# print(course[0])
# print(course[-2])
# print(course[0:3])
# print(course[:3])
# print(course[0:])
# print(course[:])

# print(id(course))
# print(id(course[0]))


# Escape Sequences
# \'
# \"
# \\
# \n

# message = 'Python\'s \nProgramming'
# print(message)


# Formated strings

# first = "Ezeh"
# last = "Ernest"
# full = f"My name is{first} {last}"
# print(full)


# Useful String Methods

# course = "Python Programming"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.lstrip())
# print(course.find("pro"))
# print(course.replace("P", "N"))
# print("Programming" in course)
# print("Programming" not in course)


# Numbers

# x = 10
# x = 0b10
# print(bin(x))


# x = 0x12c
# print(hex(x))

# # a + bi
# x = 1 + 2j
# print(x)


# 3 Arithmetic Operations

# x = 10 + 3
# x = 10 - 3
# x = 10 * 3
# x = 10 / 3
# x = 10 // 3
# x = 10 % 3
# x = 10 ** 3


# print(x)


# Working with numbers
# import math

# PI = 3.14
# print(round(PI))
# print(abs(PI))
# print(math.floor(PI))


# Type Conversion
# x = int(input("x: "))

# print(int(x))
# print(float(x))
# print(bool(x))
# print(str(x))


# Falsy
# ""
# 0
# []
# None (null)


# Conditional Statement

# age = 22
# if age >= 18:
#     print("Adult")
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")

# print("All done!")


# Logical Operator

# and
# not
# or

# name = "Ernest"

# if not name:
#     print("name is empty")

# age = 22
# # if age >= 18 and age < 65:
# if 18 <= age < 65:
#     print("Eligble")


# Ternary Operator

# age = 22

# if age >= 18:
#     message = "Eligble"
# else:
#     message = "Not eligble"


# message = "Eligble" if age >= 18 else "Not eligble"

# print(message)


# school = True

# full = "He is in school" if school == True else "Not in school"

# print(full)


# For loops

# for x in "Python":
#     print(x)


# for x in ['a', 'b', 'c']:
#     print(x)


# for x in range(0, 10, 2):
#     print(x)


# print(type(range(5000000000)))
# print([1, 2, 3, 4, 5])


# 333 For else
# names = ["John", "Mary"]
# for name in names:
#     if name.startswith("J"):
#         print("Found")
#         break
# else:
#     print("Not found")


# While looops

# guess = 0
# answer = 5

# while answer != guess:
#     guess = int(input("Guess: "))


# Functions

# def name(number: int, by: int = 1) -> tuple:
#     return (number, number + by)


# print(name(20))


# args. wait, what?

# def multiply(*list):
#     total = 1
#     for number in list:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))


# **arg

# def save_user(**user):
#     print(user["name"])

# save_user(id=1, name="admin")


# Quiz

# local variable
# def greet():
#     if True:
#         message = 'Ernest'
#     print(message)

# greet()


# Global variable

# message = 'Ernest'


# def name():
#     global message
#     message = "Escobarb"
#     print(message)

# name()





# Debugging

# def mutiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total



# print("start")
# print(mutiply(1, 2, 3))
# print("finish")




# Exercise

# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input
    

# print(fizz_buzz(5))

# orrrr

import os, time
def menu(enter):
    if (enter % 3 == 0) and (enter % 5 == 0):
        print("FizzBuzz")
    if enter % 3 == 0:
        print("Fizz")
    if enter % 5 == 0:
        print("Buzz")


menu(500)
time.sleep(3)
os.system("clear")