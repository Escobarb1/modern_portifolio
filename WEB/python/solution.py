# name = 'Ernest'
# school = 'University Of Nigeria'
# hold = f'My name is {name}. name of my school is {school}' 
# print(hold)

# price = 500
# if price < 50:
#     print('I will buy phone')
# else:
#     print('I will not buy phone')



# price = 7
# if price < 10:
#     print("I want the food")
# print("I want the drink")


# name = int(input("How many years are you? "))

# if name  > 18:
#     print("Already an adult.")
# elif name > 40:
#     print("You are an old man")
# else:
#     print("A newbie")



# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# num3 = int(input("Enter the last number: "))

# largest = num1

# if(num2 >= num1) and (num2 >= num3):
#     largest = num2
# elif(num3 >= num1) and (num3 >= num2):
#     largest = num3
# else:
#     largest = num1
# print("Largest number you entered is: ", largest)


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# num3 = int(input("Enter the last number: "))

# largest = max(num1, num2, num3)
# print("The largest number is: ",largest)




# len = int(input("How many numbers do you want to enter? "))

# nums = []

# for i in range(0, len):
#     element = int(input("Enter element: "))
#     nums.append(element)

# total = sum(nums)
# avg = total/len
# print("Average of element you entered",round(avg,2))


# len = int(input("How many numbers do you want to enter? "))

# total = 0

# for i in range(0, len):
#     elem = int(input("Enter element: "))
#     total += elem

# avg = total/len
# print("Average of element you entered",round(avg,2))


# nums = [66, 7, 3, 6, 6, 7, 9]

# def get_sum(nums):
#     sum = 0
#     for num in nums:
#         sum = sum + num
#     return sum


# total = get_sum(nums)
# print("The total of each elements: ",total)


# getting the sum of the numbers in an array
# nums = [66, 7, 3, 6, 6, 7, 9]

# total = sum(nums)
# print(total)



# def square_sum(num):
#     sum = 0
#     for i in range(num+1):
#         square = (1 ** 2)
#         sum = sum + square

#     return sum 

# num = int(input("Enter a number: "))
# sum = square_sum(num)

# print("sum of square numbers is ",sum)


# def sum_of_square(n):
#     sum = n*(n+1)*(2*n+1)/6
#     return sum


# num = int(input("Enter a number: "))
# sum = sum_of_square(num)
# print("Your sum of square is ",sum)


# finding the second highest variable

# def get_second_largest(nums):
#     largest = nums[0]
#     second_largest = nums[0]
#     for i in range(1, len(nums)):
#         if nums[i] > largest:
#             second_largest = largest
#             largest = nums[i]
#         elif nums[i] > second_largest:
#             second_largest = nums[i]
#     return second_largest


# my_nums = [44, 22, 67, 36, 82, 45]
# second_largest = get_second_largest(my_nums)
# print("Second highest number is :",second_largest)

# orr 

# my_nums = [44, 22, 67, 36, 82, 45]
# my_nums.remove(max(my_nums))
# second_largest = max(my_nums)
# print(second_largest)


# Getting the largest number
# my_nums = [44, 22, 67, 36, 82, 45, 100]
# my_nums = sorted(my_nums)
# print(my_nums[-1])


# Reverse index
# my_nums = [44, 22, 67, 36, 82, 45]
# print(my_nums[-1])
# print(my_nums[-2])
# print(my_nums[-3])


# # orr

# my_nums = [44, 22, 67, 36, 82, 45]
# my_nums.sort(reverse=True)
# print(my_nums[1])


# Getting the second smallest element

# my_nums = [44, 22, 67, 36, 82, 45]
# my_nums.remove(min(my_nums))
# second_smallest = min(my_nums)
# print("The second smallest value in the array is",second_smallest)

# orr

# my_nums = [44, 22, 67, 36, 82, 45]
# my_nums = sorted(my_nums)
# print(my_nums[1])


# Removing all the duplicated characters from a string


# def remove_duplicate(names):
#     result = ''
#     for name in names:
#         if name not in result:
#             result += name
#     return result


# user_input = input("What is your string: ")

# no_duplicate = remove_duplicate(user_input)
# print("Without duplicate: ",no_duplicate)





# CONVERSION


# Miles to kilometers
# miles = int(input("Enter distance in miles:"))
# kg = miles * 1.609344
# print("Distance in Kilometers",kg)



# COMPUTATION


# simple interest

# principal = int(input("Money borrowed: "))
# years = float(input("interest Rate: "))
# rate = float(input("Overall Duration: "))

# simple_interest = (principal * years * rate) / 100
# print('$',simple_interest)


# Compound interest

# principal = float(input("Money borrowed: "))
# years = float(input("interest Rate: "))
# rate = float(input("Overall Duration: "))

# compound_interest = principal * (1 + rate / 100)**years
# print('$',compound_interest)


# orrm


# def compound_interest(principle, rate, time):
#     interest = principle * ((1 + rate / 100)** time)
#     return interest


# principle = float(input("Money borrowed: "))
# time = float(input("interest Rate: "))
# rate = float(input("Overall Duration: "))

# total_due = compound_interest(principle, rate, time)
# print('Interest Amount is $:',total_due)


# cal grade
# def average_grade(first_grade, second_grade, third_grade, fourth_grade, fifth_grade):
#     average = first_grade + second_grade + third_grade + fourth_grade + fifth_grade / 5
#     return average


# first_grade = int(input("Enter the first grade: "))
# second_grade = int(input("Enter the second grade: "))
# third_grade = int(input("Enter the third grade: "))
# fourth_grade = int(input("Enter the fourth grade: "))
# fifth_grade = int(input("Enter the last grade: "))

# total = average_grade(first_grade, second_grade, third_grade, fourth_grade, fifth_grade)
# print("The average is:",total)





# print('Input your marks:')
# sub1 = int(input('First Subject: '))
# sub2 = int(input('Second Subject: '))
# sub3 = int(input('Third Subject: '))
# sub4 = int(input('Fourth Subject: '))
# sub5 = int(input('Fifth Subject: '))

# average = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

# if average >= 90:
#     print("Grade: A")
# elif average >= 80:
#     print('Grade: B')
# elif average >= 70:
#     print('Grade: C')
# elif average >= 60:
#     print('Grade: D')
# else:
#     print('Grade: F')





# cal gravitational force

# def gravitational_force(G, m1, m2, r):
#     force = (G * m1 * m2) / (r ** 2)
#     return force


# print('Enter the following inputs correctly:')
# G = 6.673*(10**-11)
# m1 = int(input('Enter the first mass: '))
# m2 = int(input('Enter the second mass: '))
# r = int(input('Enter the distance between the two the masses: '))

# gravity = gravitational_force(G, m1, m2, r)
# print('The gravitational force is:',gravity)





# Triangle Area

# import math

# a = float(input('Enter the side: '))
# b = float(input('Enter the second side: '))
# c = float(input('Enter the third side: '))

# # cal the semi-perimeter
# s = (a + b + c) / 2

# # cal the area
# area = math.sqrt(s*(s-a)*(s-b)*(s-c))
# print('Area of your triangle is',area)









# prime number

# def prime_number(number):
#     for i in range(2, number):
#         if (number % i) == 0:
#                 return False
#         return True



# number = int(input('Enter a number: '))

# check_prime = prime_number(number)

# if check_prime:
#     print('The number entered is a prime number.')
# else:
#         print("Number entered is not a prime number.") 




# All prime numbers
# def prime_number(number):
#     for i in range(2, number):
#         if (number % i) == 0:
#                 return False
#         return True
    

# def all_primes(number):
#     primes = []
#     for n in range(2,number+1):
#          if prime_number(n) is True:
#               primes.append(n)
#     return primes

# number = int(input('Enter upper limit: '))
# primes = all_primes(number)
# print(primes)




# prime factors

# def get_prime_factors(n):
#     factors = []
#     divisor = 2
#     while n > 2:
#         if(n % divisor == 0):
#             factors.append(divisor)
#             n = n / divisor
#         else:
#             divisor = divisor + 1
#     return factors


# num = int(input('Enter your number: '))
# factors = get_prime_factors(num)
# print(factors)



















# Data structure

# stack

# heroes = []
# heroes.append('T-shirt')
# heroes.append('shirt')
# heroes.append('sweater')
# print(heroes)

# pop

# clothes = ['t-shirt', 'shirt', 'sweater', 'jacket']
# first = clothes.pop() 
# second = clothes.pop()
# print(first)
# print(second)




# creating a queue

# lines = [ ]
# lines.append('Putin')
# lines.append('Trump')
# lines.append('Merkel')
# print(lines)


# removing element from a list
# lines = ['Putin', 'Trump', 'Kim Jong', 'Merkel']
# first = lines.pop(0)
# second = lines.pop(0)
# print(first)
# print(second)
# print(lines)





# dictionaries

# result = {'John' : 81, 'Tim' : 90}
# timScore = result['Tim']
# print(timScore)



# # removing a dictionary
# scores = {'John': 81, 'Tim' : 75}
# del scores['John']
# print(scores)




# reverse

# def reverse_string(str):
#     reverse = ''
#     for char in str:
#         reverse = char + reverse
#     return reverse


# str = input('Enter your string: ')
# result = reverse_string(str)
# print(result)


# orr


# def reverse_recur(str):
#     if len(str) == 0:
#         return str
#     else:
#         return reverse_recur(str[1:]) + str[0]
    

# str = input('Enter a string: ')
# rev_str = reverse_recur(str)
# print('Reverse of your string: ',rev_str)



# orrr


# txt = input('Enter a string: ')
# str = txt
# print(str[::-1])


# getting palindrome

# str = input('Enter a string: ')
# rev = str[::-1]
# if (rev == str):
#     print('Is a palindrome.')
# else:
#     print('Is not a palindrome.')



# getting gcd


# def gcd(a, b):
#     if (b==0):
#         return a 
#     else:
#         return gcd(b, a % b)
    

# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# GCD = gcd(a, b)
# print('GCD is: ',GCD)


# orr

# import math

# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))

# gcd = math.gcd(a, b)
# print(gcd)




# A simple guessing game

# print('To stop anytime, enter: 79')
# number  = int(input('Enter a number from 1 to 100: '))
# guess = 79
# if (number  >= 10):
#     print('Number is too small.')
# elif (number >= 20):
#     print('Number is too small.')
# elif (number >= 30):
#     print('Number is too small.')
# elif (number >= 40):
#     print('Number is too small.')
# elif (number >= 50):
#     print('Number is too small.')
# elif (number >= 60):
#     print('Number is too small.')
# elif (number >= 70):
#     print('Number is too small.')
# elif (number >= 75):
#     print('Number is too small.')
# elif (number >= 76):
#     print('Number is too small.')
# elif (number >= 77):
#     print('Number is too small.')
# elif (number >= 78):
#     print('Number is too small.')
# elif (number >= 79):
#     print('----Oppps, You got it right----')
# elif (number >= 80):
#     print('Number is too big.')
# elif (number >= 90):
#     print('Number is too big.')
# elif (number >= 100):
#     print('Number is too big.')

# print(number)





# Rock paper scissor game

# def get_winner(p1, p2):
#     if p1 == p2:
#         return "It's a tie"
#     elif p1 == 'Rock':
#         if p2 == 'scissors':
#             return 'First player wins!'
#         else:
#             return 'Second'
#     elif p1 == 'scissors':
#         if



