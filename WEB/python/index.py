import math
# print('Ernest')
# print('o----')
# print(' ||||')
# print('*' * 10)
# price = 10
# price = 20
# print(price)
# ernest = 'paraclete'
# print('the name of my school is ' + ernest)
# rating = 4.0
# print(rating)
# is_published = True
# print(is_published)

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2023 - int(birth_year)
# print(type(age))
# print(age)

# weight = input('user weight: ')
# kg = int(weight) * 20
# print(kg)

# course = 'Python for Beginners'
# print(course[0:5])

# first = 'John'
# last = 'Smith'
# msg = first + ' [' + last + '] is a coder'
# message = f'{first} [{last}] is a coder'
# print(msg)
# print(message)

# x = 2.9
# print(round(x))

# print(abs(-2.9))

# print(math.ceil(2.9))
# print(math.floor(2.9))


# if statement
# is_hot = True
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print('Drink plenty of water')
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:  
#     print("It's a lovely day")
# print("Enjoy your day")

# price = 1000000
# has_good_credit = True

# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")


# logical (AND) operator #Both conditions must be true
# has_high_income = True
# has_good_credit = True

# if has_high_income and has_good_credit:
#     print("Eligble for loan")


# logical (OR) operator # at least one condition must be true
# has_high_income = False
# has_good_credit = True

# if has_high_income or has_good_credit:
#     print("Eligble for loan")


#logical (AND NOT) operator #one true another false
# has_good_credit = True
# has_criminal_record = False

# if has_good_credit and not has_criminal_record:
#     print("Eligble for loan")



# temperature = 39
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")




def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input
    

print(fizz_buzz(5))