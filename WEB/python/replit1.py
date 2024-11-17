# print("Uh, oh, you've been given a" "\033[31m", 'warning', '\033[0m', 'for being a bad, bad person')



#####secure password

# print("SECURE LOGIN")
# print()
# username = input("Username \n > ")
# password = input("Password \n > ")

# if username == "mark" and password == 'password':
#   print("Welcome Mark!")
# elif username == "Escobarb" and password == 'Escobarb':
#   print("Hey, there Escobarb!")
# else:
#   print("Go away!")




# indenting

# tvShow = input("What is your favourite tv show? ")
# if tvShow == "money heist":
#   print("Ugh, why?")
#   faveCharacter = input("Who is your favourite character? ")
#   if faveCharacter == "professor":
#     print("Right answer")
#     professor = input("Why is professor your best character? ")
#     print("Thanks for your review!")
#   else:
#     print("Ugh,  proffessor the greatest")
# elif tvShow == "prison break":
#   print("Aww, sad times")
#   prison = input("Who is your favourite character?")
#   if prison == "michael":
#     print("Aww, that's true!")
#   else:
#     print("michael scofid is the greatest!")
# else:
#   print("Yeah, that's cool and all...")



# Generational Identifier

# birthYear = int(input("What year were you born? \n >> "))
# if birthYear <= 1946:
#   print("You are a Traditionalist.")
# elif birthYear >= 1947 and birthYear <= 1964:
#   print("Hey, Baby Boomer! How you doing?")
# elif birthYear >= 1965 and birthYear <= 1981:
#   print("Gen X! What's up?")
# elif birthYear >= 1982 and birthYear <= 1995:
#   print("Millenials! The age of tech!")
# elif birthYear >= 1996:
#   print("Hey, Gen Z! TikTok much?")
# else: 
#   print("Try again!")







  # split the bill

# myBill = float(input("What was the bill?: "))
# numberOfPeople = int(input("How many people?: "))
# answer = myBill / numberOfPeople
# answer = round(answer, 2)
# print("You all owe", answer)





# myBill = float(input("What was the bill?: "))
# numberOfPeople = int(input("How many people?: "))
# tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent? "))


# bill_with_tip = tip / 100 * myBill + myBill
# bill_per_person = bill_with_tip / numberOfPeople
# final_amount = round(bill_per_person, 2)


# print("You all owe", final_amount)







# cal how seconds are in a year
# days_this_year = int(input("How many days are in this year? "))
# days_in_year = 365
# days_in_leapyear = 366
# hours_in_day = 24
# minute_in_hour = 60
# seconds_in_minute = 60

# result = days_in_year * hours_in_day * minute_in_hour * seconds_in_minute
# leapyear_result = days_in_leapyear *  hours_in_day * minute_in_hour * seconds_in_minute

# if days_in_year == 366:
#   print("Number of seconds in a leap year is ",leapyear_result)
# else:
#   print("Number of seconds in a year is ",result)






# Exam grade builder

# print("Exam Grade Calculator")
# print()
# exam_name = input("Name of exam? ")
# print()
# score = int(input("Maximum possible score? "))
# your_score = float(input("What is your score? "))

# percentage = (your_score / score) * 100
# answer = round(percentage, 2)
# if answer >= 90:
#   print(f"You got {answer}% which is A+")
# elif answer >= 80 and answer <= 89:
#   print(f"You got {answer}% which is A")
# elif answer >= 70 and answer <= 79:
#   print(f"You got {answer}% which is C")
# elif answer >= 60 and answer <= 69:
#   print(f"You got {answer}% which is B")
# elif answer >= 50 and answer <= 59:
#   print(f"You got {answer}% which is D")
# elif answer <= .49:
#   print(f"You got {answer}% which is U")
# else:
#   print("Try again!")






# print("E P I C    🪨  📄 ✂️   B A T T L E ")
# print()
# print("Select your move (R, P or S)")
# print()

# player1Move = input("Player 1 > ")
# print()
# player2Move = input("Player 2 > ")
# print()

# if player1Move=="R":
#   if player2Move=="R":
#     print("You both picked Rock, draw!")
#   elif player2Move=="S":
#     print("Player1 smashed Player2's Scissors into dust with their Rock!")
#   elif player2Move=="P":
#     print("Player1's Rock is smothered by Player2's Paper!")
#   else:
#     print("Invalid Move Player 2!")
# elif player1Move=="P":
#   if player2Move=="R":
#     print("Player2's Rock is smothered by Player1's Paper!")
#   elif player2Move=="S":
#     print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
#   elif player2Move=="P":
#     print("Two bits of paper flap at each other. Dissapointing. Draw.")
#   else:
#     print("Invalid Move Player 2!")
# elif player1Move=="S":
#   if player2Move=="R":
#     print("Player 2's Rock makes metal-dust out of Player1's Scissors")
#   elif player2Move=="S":
#     print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
#   elif player2Move=="P":
#     print("Player1's Scissors make confetti out of Player2's paper!")
#   else:
#     print("Invalid Move Player 2!")
# else:
#   print("Invalid Move Player 1!")











# exit = ""
# while exit != "yes":
#   print("🥳")
#   exit = input("Exit?: ")





# exit = "no"


# while exit == "no":
#   animal_sound = input("What animal sound do you want to hear?")
  
#   if animal_sound == "cow" or animal_sound == "Cow":
#     print("🐮 Moo")
#   elif animal_sound == "pig" or animal_sound == "Pig":
#     print ("🐷 Oink")
#   elif animal_sound == "sheep" or animal_sound == "Sheep":
#     print ("🐑 Baaa")
#   elif animal_sound == "duck" or animal_sound == "Duck":
#     print("🦆 Quack")
#   elif animal_sound == "dog" or animal_sound == "Dog":
#     print("🐶 Woof")
#   elif animal_sound == "cat" or animal_sound == "Cat":
#     print("🐱 Meow")
#   else: 
#     print("I don't know that animal sound. Try again.")


#   exit = input("Do you want to exit?: ")







# Name the lyrics

# print("Fill in the blank lyrics! (Type in th eblamk lyrics and see if you are as cool as me.)")
# print()
# print("Figure out the missing word as quickly as you can!")
# print()

# counter = 1
# while True:
#   print("I don't wanna _______ too high and might, cause tomorrow i may fall down on my face.")
#   lyrics = input(">>  ")
#   if lyrics == "act" or lyrics == "Act":
#     print("You got it right!")
#   else:
#     print("Nope! Try again!")
#     counter += 1
#   if lyrics == "act":
#     break
# print("Thanks for playing!")

# print("You got the correct lyrics in ", counter, "attempt(s).")














# while loop


# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
#     exit()
# print("The game is over, you've failed!")






# print("Welcome to Guess the Number.")
# print()
# print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
# print()
# print("Let's play!")

# number = 2300
# attempt = 1

# while True:
#   print("Pick a number between 1 and 1,000,000: ")
#   guess = input(">>  ")
#   if guess < 0:
#     print("Now we'll never know what the answer is …")
#     exit()
#   if guess < number:
#     print("That number is too low. Try again!.")
#     attempt += 1
#   elif guess > number:
#     print("The number is too high. Try again!.")
#     attempt += 1
#     continue
#   elif guess == number:
#     print('''
#     --You are the winner--
#       you got it right ''')
#     break
#   else:
#     print("That is not a number i recognize.")
# print("Thanks for playing!")

# print("It took you", attempt, "attempt(s) to get the correct answer.")




# print("Welcome to Guess the Number.")
# print()
# print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
# print()
# print("Let's play!")

# import random
# attempt = 1
# correct_number = random.randint(1, 1000000)
# # correct_number = 2300

# while True:
#   user_guess = int(input("Pick a number between 1 and 1,000,000: "))
#   if user_guess < 0:
#     print("Now we'll never know what the answer is …")
#     exit()
#   if user_guess < correct_number:
#     print("That number is too low. Try again!")
#     attempt += 1
#   elif user_guess > correct_number:
#     print("That number is too high. Try again!")
#     attempt += 1
#     continue
#   elif user_guess == correct_number:
#     print("You are a winner! 🥳🥳")
#     break 
#   else:
#     print("That is not a number I recognize.")
# print("It took you", attempt, "attempt(s) to get the correct answer.")









# for loop

# loan = 1000
# apr = 0.05
# for i in range(10):
#   loan+=(loan*apr)
#   print("Year", i+1, "is", round(loan,2))










# List generator

# print("List Generator!")
# print()
# start = int(input("Start at: "))
# end = int(input("End before: "))
# increment = int(input("Increment between values: "))
# print()
# print()
# for i in range(start, end, increment):
#   print(i)









# multiplication game

# print("Welcome to Math Facts Game")
# print()
# print("How well do you know your math facts? Pick a number and I will give you 10 math facts to solve.")
# print()

# fact_family = int(input("Name your multiples: "))
# print()

# counter = 0
# for i in range(1, 11):
#   correct_answer = i * fact_family 
#   print(i, "x", fact_family)
#   answer = int(input("> "))
#   if answer == correct_answer:
#     print("You got it right!")
#     counter += 1
#   else:
#     print(f"That's not correct. It should have been {correct_answer}")
    
# if counter == 10:
#   print("Wow! A perfect score! 🥳")
# else:
#   print(f"You got {counter} out of 10 correct.")



# def rollDice():
#   import random
#   dice = random.randint(1, 6)
#   print("You rolled", dice)


# rollDice()









# print("Replit Login System")
# print()
# def login():
#   while True:
#     print("What is your username? ")
#     username = input(">>> ")
#     print("What is your password? ")
#     password = input(">>> ")
#     if username == "Escobarb" and password == "Pablo":
#       print("Welcome Escobarb!")
#       break
#     else:
#       print("That is not the correct username or password. Try again!")
#       continue


# print("REPLIT LOGIN SYSTEM")
# login()














# print("30 Days Down: What do you think?")
# print()
# for i in range(1, 31):
#   question = input(f"Day {i}:\n>> ")
#   print()
#   myText = f"You thought Day {i} was"
#   print(f"{myText:^35}")
#   print(f"{question:^35}")
#   print()






# import os, time

# for i in range(1, 101):
#   print(i)
#   time.sleep(0.5)
#   os.system("clear")



# import os, time
# print('\033[?25l', end="")
# for i in range(1, 101):
#   print(i)
#   time.sleep(0.2)
#   os.system("clear")















# print("Character Stats Generator")
# print()
# import random
# def rollDice(sides):
#   result = random.randint(1, sides)
#   return result


# def roll_6_and_8():
#   roll_6_sided_dice = rollDice(6)
#   roll_8_sided_dice = rollDice(8)
#   health = roll_6_sided_dice * roll_8_sided_dice
#   return health


# print("⚔️Character stats generator⚔️")


# haveACharacter = "yes"
# while haveACharacter == "yes":
#   character = input("Name your warrior: ")
#   health = str(roll_6_and_8())
#   print("Their health is ", health,"hp" ) 
#   haveACharacter = input("Want to create another character?")






















# import os
# for i in range(1,1000):
#   print(i)

# os.system("clear")

# import os, time
# print("Welcome")
# print("to")
# print("Replit")

# time.sleep(1)
# os.system("clear")

# username = input("Username: ")
# print(f"Nice having you, {username}")



















# from replit import audio
# import os, time

# def play():
#   source = audio.play_file('audio.wav')
#   source.paused = False # unpause the playback
#   while True:
#     stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : ")) # giving the user the option to stop playback
#     if stop_playback == 2:
#       source.paused = True # let's pause the file 
#       return # let's go back from this play() subroutine
#     else: 
#       continue
  
# while True:
#   os.system("clear")
#   print("🎵 MyPOD Music Player ")
#   time.sleep(1)
#   print("Press 1 to Play")
#   time.sleep(1)
#   print("Press 2 to Exit")
#   time.sleep(1)
#   print("Press anything else to see the menu again")
#   userInput = int(input())
#   if userInput == 1:
#     print("Playing some proper tunes!")
#     play()
#   elif userInput == 2:
#     exit()
#   else :
#     continue


















# for i in range(0, 100):
#   print(i)



# for i in range(0, 100):
#   print(i, end=", ")


#new line
# for i in range(0, 100):
#   print(i, end="\n")


#tab indent
# for i in range(0, 100):
#   print(i, end="\t")



#vertical tab
# for i in range(0, 100):
#   print(i, end="\v")




# print("If you put")
# print("\033[33m", end="") #yellow
# print("nothing as the")
# print("\033[35m", end="") #purple
# print("end character")
# print("\033[32m", end="") #green
# print("then you don't")
# print("\033[0m", end="") #default
# print("get odd gaps")


# print("If you put", "\033[33m", "nothing as the", "\033[35m", "end character", "\033[32m", "then you don't", "\033[0m", "get odd gaps", end="")




# print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")

# import os

# for i in range(1, 101):
#   print(i)
#   os.system("clear")






















# def colorChange(color):
#   if color=="red":
#     return ("\033[31m")
#   elif color=="white":
#     return ("\033[0m")
#   elif color=="blue":
#     return ("\033[34m")
#   elif color=="yellow":
#     return ("\033[33m")
#   elif color == "green":
#     return ("\033[32m")
#   elif color == "purple":
#     return ("\033[35m")

# title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="

# print(f"        {title:^35}")
# print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
# print(f"\t{colorChange('yellow')}Queen")

# prev = "prev"
# next = "next"
# pause = "pause"

# print(f"{colorChange('white')}{prev:<35}")
# print(f"{colorChange('green')}{next:^35}")
# print(f"{colorChange('purple')}{pause:>35}")


# print()
# print()
# text = "WELCOME TO"
# print(f"{colorChange('white')}{text:^35}")
# text = "--  ARMBOOK  --"
# print(f"{colorChange('blue')}{text:^35}")
# text = "Definitely not a rip off"
# print(f"{colorChange('yellow')}{text:>35}")
# text = "a certain other social"
# print(f"{colorChange('yellow')}{text:>35}")
# text = "networking site"
# print(f"{colorChange('yellow')}{text:>35}")
# text = "Honest."
# print(f"{colorChange('red')}{text:^35}")
# text = "Username: "
# username = input(f"{colorChange('white')}{text:^35}")
# text = "Password: "
# username = input(f"{colorChange('white')}{text:^35}")











































# greeting in the different languages
# import random
# greetings = ["Hello there!", "Konnichiwa", "Guten Tag!", "Bore Da!"]
# index = random.randint(0,3)
# print(greetings[index])






































# myAgenda = []

# def printList():
#   print() #this is just to add an extra space between items
#   for item in myAgenda:
#     print(item)
#   print() #this is just to add an extra space between items

# while True:
#   item = input("What's next on the Agenda?: ")
#   myAgenda.append(item)
#   printList()




# myAgenda = []

# def printList():
#   print() 
#   for item in myAgenda:
#     print(item)
#   print() 

# while True:
#   menu = input("add or remove?: ")
#   if menu == "add":
#     item = input("What's next on the Agenda?: ")
#     myAgenda.append(item)
#   elif menu == "remove":
#     item = input("What do you want to remove?: ")
#     myAgenda.remove(item)
#   printList()



# import os, time
# toDoList = []

# def printList():
#   print()
#   for item in toDoList:
#     print(item)
#   print()

# while True:
#   menu = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n")
#   if menu=="view":
#     printList()
#   elif menu=="add":
#     item = input("What do you want to add?\n")
#     toDoList.append(item)
#   elif menu=="edit":
#     item = input("What do you want to remove?\n")
#     if item in toDoList:
#       toDoList.remove(item)
















# timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
# print(timetable[3])



# timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
# print(timetable[0])
# print(timetable[1])
# print(timetable[2])
# print(timetable[3])
# print(timetable[4])





# timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
# for lesson in timetable:
#   print(lesson)



# import random
# greetings = ["Hello there!", "Konnichiwa", "Guten Tag!", "Bore Da!"]
# index = random.randint(0,3)
# print(greetings[index])


































# import os, time
# listOfEmail = []

# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#   time.sleep(1)
#   os.system("clear")




# import os, time
# listOfEmail = []

# def prettyPrint():
#   os.system("clear") 
#   print("listofEmail") 
#   print()
#   counter = 1 # add a counter
#   for email in listOfEmail: 
#     print(f"{counter}: {email}") # make this an f-string
#     counter += 1 # adds a number with each new email
#   time.sleep(1)

# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#   elif menu == "3":
#     prettyPrint()  
#   time.sleep(1)
#   os.system("clear")





# import os, time
# listOfEmail = []

# def prettyPrint():
#   os.system("clear") 
#   print("listofEmail") 
#   print()
#   for index in range(len(listOfEmail)): # len counts how many items in a list
#     print(f"{index}: {listOfEmail[index]}") 
#   time.sleep(1)


# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#   elif menu == "3":
#     prettyPrint() 
#   time.sleep(1)
#   os.system("clear")









# import os, time
# listOfEmail = []

# def prettyPrint():
#   os.system("clear")
#   print("listOfEmail")
#   print()
#   counter = 1
#   for email in listOfEmail:
#     print(f"{counter}: {email}")
#     counter+=1
#   time.sleep(1)

# def spam(max):
#   for i in range(0,max):
#     print(f"""Email {i+1}

# Dear {listOfEmail[i]}
# It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

# Love and hugs,

# Ian Spammington III""")
#     time.sleep(1)
#     os.system("clear")
# while True:
#   print("SPAMMER Inc.")
#   menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu== "2":
#     email = input("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#   elif menu == "3":
#     prettyPrint()
#   elif menu =="4":
#     spam(10)
#   time.sleep(1)
#   os.system("clear")
















# import time, os
# print("TODO LIST MANAGER")
# print()
# to_do_list = []

# def printList():
#   for items in to_do_list:
#     print(item)
#   print()



# while True:
#   menu = input("Do you want to view, add, remove or edit the todo list\n =>  ")
#   if menu == "view":
#     print(printList)
#   elif menu == "add":
#     item = input("What do you want to add?\n =>  ")
#     to_do_list.append(item)
#   elif menu == "remove":
#     item = input("Are you sure you want to remove this?\n =>  ")
#     if item[0] == "y":
#       if item in to_do_list:
#         to_do_list.remove(item)
#   elif menu == "delete":
#     to_do_list = []
#   time.sleep(2)
#   os.system("clear")



















# name = input("What's your name? ")
# if name.lower().strip() == "david": 
#   print("Hello Baldy!")
# else: 
#   print("What a beautiful head of hair!")




# surName = input("what is your surname? \n=> ").capitalize()
# firstName = input("What is your first name? \n=> ").capitalize()
# print()
# print(f"{surName} {firstName}")



# rolodex = []
# def printList():
#   print()
#   for name in rolodex:
#     print(name)
#   print()

# while True:
#   surName = input("what is your surname? \n=> ").capitalize().strip()
#   firstName = input("What is your first name? \n => ").capitalize().strip()
#   print() 
#   name = f"{surName} {firstName}"
#   if name not in rolodex:
#     rolodex.append(name)
#   else:
#     print("ERROR: Duplicate name")
#   printList()






















# print("🌟Star Wars Name Generator🌟")
# print()

# firstName = input("Input your first name?\n => ").title()
# lastName = input("Input your last name?\n => ").lower()
# mother = input("Input your mother's maiden name?\n => ").title()
# city = input("Input the city where you were born?\n => ").lower() 

# first = firstName[:3].strip()
# second = lastName[:3].strip()
# maiden = mother[:2].strip()
# town = city[-3:].strip()

# print(f"your star name is {first} {second} {maiden} {town}")



# print("STAR WARS NAME GENERATOR")

# all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()

# first = all[0].strip()
# last = all[1].strip()
# maiden = all[2].strip()
# city = all[3].strip()

# name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

# print(f"Your Star Wars name is {name}")































# import random, os, time

# listOfWords = ["apple", "orange", "grapes", "pear"]
# letterPicked = []
# lives = 6

# word = random.choice(listOfWords)

# while True:
#   time.sleep(1)
#   os.system("clear")
#   letter = input("Choose a letter: ").lower()
  
#   if letter in letterPicked:
#     print("You've tried that before")
#     continue
    
#   letterPicked.append(letter)
  
#   if letter in word:
#     print("You found a letter")
#   else:
#     print("Nope, not in there")
#     lives -= 1
  
#   allLetters = True
#   print()
#   for i in word:
#     if i in letterPicked:
#       print(i, end="")
#     else:
#       print("_", end="")
#       allLetters = False
#   print()

#   if allLetters:
#     print(f"You won with {lives} left!")
#     break

#   if lives<=0:
#     print(f"You ran out of lives! The answer was {word}")
#     break
#   else:
#     print(f"Only {lives} left")