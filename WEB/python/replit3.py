# f = open("savedFile.txt", "w")
# f.write("Enter your username?")
# text = input("=> ")
# f.write(text)
# f.close()


# f = open("savedFile.txt", "a+")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# f.close()








# PROJECT
# import os,time

# while True:
#   print("🌟HIGH SCORE TABLE🌟")
#   print()
#   initials = input("What is your initials => ").upper()
#   score = input("What is your score => ")
#   print()
  
#   f = open("high.score", "a+")
#   f.write(f"{initials} {score}\n")
#   f.close()
#   time.sleep(3)
#   os.system("clear")




# f = open("filenames.list", "r")
# contents = f.read()
# f.close()

# contents = contents.split() #added split here

# print(contents)









# f = open("filenames.list","r")
# contents = f.readline()
# print(contents)

# f.close()
















# myEvents = []

# def prettyPrint():
#   print()
#   for row in myEvents:
#     print(f"{row[0] :^15} {row[1] :^15}")
#   print()

# while True:
#   menu = input("1: Add, 2: Remove\n")

#   if menu == "1":
#     event = input("What event?: ").capitalize()
#     date = input("What date?: ")
#     row = [event,date]
#     myEvents.append(row)
#     prettyPrint()

#   else:
#     criteria = input("What event do you want to remove?: ").title()
#     for row in myEvents:
#       if criteria in row:
#         myEvents.remove(row)

#   f = open("calendar.txt", "w")
#   f.write(str(myEvents))
#   f.close()











# import os, time, random

# def add():
#   os.system("clear")
#   idea = input("Idea > ")
#   f = open("my.ideas", "a+")
#   f.write(f"{idea}\n")
#   f.close()
#   time.sleep(1)
#   os.system("clear")

# def show():
#   os.system("clear")
#   f = open("my.ideas", "r")
#   ideas = f.read().split("\n")
#   f.close()
#   ideas.remove("")
#   idea = random.choice(ideas)
#   print(idea)
#   time.sleep(2)
#   os.system("clear")

# while True:
#   menu = input("1: Add idea\n2: Show a random idea\n> ")
#   if menu == "1":
#     add()
#   else:
#     show()












# myEvents = []

# def prettyPrint():
#   print()
#   for row in myEvents:
#     print(f"{row[0] :^15} {row[1] :^15}")
#   print()

# while True:
#   menu = input("1: Add, 2: Remove\n")

#   if menu == "1":
#     event = input("What event?: ").capitalize()
#     date = input("What date?: ")
#     row = [event,date]
#     myEvents.append(row)
#     prettyPrint()

#   else:
#     criteria = input("What event do you want to remove?: ").title()
#     for row in myEvents:
#       if criteria in row:
#         myEvents.remove(row)

#   f = open("calendar.txt", "w")
#   f.write(str(myEvents))
#   f.close()





















# ### Project

# # | Name | Date | Priority
# import os, time
# todo = []
# # f = open("to.do", "r")
# # todo = eval(f.read())
# # f.close()

# def add():
#   time.sleep(1)
#   os.system("clear")
#   name = input("Name > ")
#   date = input("Due Date > ")
#   priority = input("Priority > ").capitalize()
#   row = [name, date, priority]
#   todo.append(row)
#   print("Added")

# def view():
#   time.sleep(1)
#   os.system("clear")
#   options = input("1: All\n2: By Priority\n> ")
#   if options=="1":
#     for row in todo:
#       for item in row:
#         print(item, end=" | ")
#       print()
#     print()
#   else:
#     priority = input("What priority? > ").capitalize()
#     for row in todo:
#       if priority in row:
#         for item in row:
#           print(item, end=" | ")
#         print()
#     print()
#   time.sleep(1)

# def edit():
#   time.sleep(1)
#   os.system("clear")
#   find = input("Name of todo to edit > ")
#   found = False
#   for row in todo:
#     if find in row:
#       found = True
#   if not found:
#     print("Couldn't find that")
#     return
#   for row in todo:
#     if find in row:
#       todo.remove(row)
#   name = input("Name > ")
#   date = input("Due Date > ")
#   priority = input("Priority > ").capitalize()
#   row = [name, date, priority]
#   todo.append(row)
#   print("Added")

# def remove():
#   time.sleep(1)
#   os.system("clear")
#   find = input("Name of todo to remove > ")
#   for row in todo:
#     if find in row:
#       todo.remove(row)

# while True:
#   menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
#   if menu == "1":
#     add()
#   elif menu == "2":
#     view()
#   elif menu == "3":
#     edit()
#   else:
#     remove()

#   time.sleep(1)
#   os.system("clear")
#   f = open("to.do", "w")
#   f.write(str(todo))
#   f.close()





####### Debuging

# myStuff = []

# try:
#   f.open("Stuff.mine","r")
#   myStuff = eval(f.read())
#   f.close()
# except Exception as err:
#   print("ERROR: Unable to load")
#   print(err)

# for row in myStuff:
#   print(row)






# debugMode = False
# myStuff = []

# try:
#   f.open("Stuff.mine","r")
#   myStuff = eval(f.read())
#   f.close()
# except Exception as err:
#   print("ERROR: Unable to load")
#   if debugMode:
#     print(traceback)

# for row in myStuff:
#   print(row)



# while True:
#   print("😀Personal Information😀")
#   print()
#   name = input("Input your full name?\n=> ")
#   age = input("Input your age?\n=> ")
#   dob = input("Date of birth?\n=> ")
#   print(f"""{name:^30}
#   {age:^30}
#   {dob:^30}
#   """)






















##### Project

# import os, time
# pizza = []

# try:
#   f = open("pizza.txt", "r")
#   pizza = eval(f.read())
#   f.close()
# except:
#   print("ERROR: No existing pizza list, using a blank list")

# def viewPizza():
#   h1 = "Name"
#   h2 = "Topping"
#   h3 = "Size"
#   h4 = "Quantity"
#   h5 = "Total"
#   print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}{h5:^10}")
#   for row in pizza:
#     print(f"{row[0]:^10}{row[1]:^20}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
#   time.sleep(2)

# def addPizza():
#   time.sleep(1)
#   os.system("clear")
#   name = input("Name: ")
#   toppings = input("Toppings: ")
#   size = input("Size (s/m/l): ").lower()
#   while True:
#     try:
#       qty = int(input("Quantity: "))
#       break
#     except:
#       print("Error: Quanity must be a whole number")
#   cost = 0
#   if size=="s":
#     cost = 5.99
#   elif size=="m":
#     cost = 9.99
#   else:
#     cost = 14.99
#   total = cost * qty
#   total = round(total, 2)
#   row = [name, toppings, size, qty, total]
#   pizza.append(row)

# while True:
#   time.sleep(1)
#   os.system("clear")
#   print("Rominos Pizza")
#   print()
#   menu = input("1: Add Pizza\n2: View Pizzas\n> ")
#   if menu == "1":
#     addPizza()
#   else:
#     viewPizza()
#   f = open("pizza.txt", "w")
#   f.write(str(pizza))
#   f.close()




































###### project 

# import os, time
# todo = []

# try:
#   f = open("inventory.txt", "r")
#   todo = eval(f.read())
#   f.close()
# except:
#   pass
  
# def add():
#   time.sleep(1)
#   os.system("clear")
#   print("🌟INVENTORY🌟")
#   print("  ==========")
#   print()
#   que = input("Are you sure you want to add => ")
#   if que[0] == "y":  
#     name = input("Input the item to add: => ").capitalize()
#     todo.append(name)
#   print(f"{name} has been added to your inventory.")
#   time.sleep(1)
#   os.system("clear")


# def remove():
#   time.sleep(1)
#   os.system("clear")
#   print("🌟INVENTORY🌟")
#   print("  ==========")
#   print()
#   reve = input("Input the item to remove: => ")
#   que = input(f"Are you sure you want to remove {reve}? ")
#   if que[0] == "y" and reve in todo:
#     todo.remove(reve)
#   print(f"{reve} has been removed from your inventory.")
#   time.sleep(1)
#   os.system("clear")


# def view():
#   time.sleep(1)
#   os.system("clear")
#   print("🌟INVENTORY🌟")
#   print("  ==========")
#   print()
#   print(todo)
#   time.sleep(1)
#   os.system("clear")
  
  


# while True:
#   time.sleep(1)
#   os.system("clear")
#   print("🌟INVENTORY🌟")
#   print("  ==========")
#   print()
#   menu = input("1. Add\n2. View\n3. Remove\n=> ")
#   if menu == "1":
#     add()
#   elif menu == "2":
#     view()
#   elif menu == "3":
#     remove()


#   f = open("inventory.txt", "w")
#   f.write(str(todo))
#   f.close()









# import csv # Imports the csv library

# with open("January.csv") as file: # Opens the csv file
#   reader = csv.reader(file) # reads the contents of the csv file into the 'reader' variable
#   line = 0

#   for row in reader: # loop to output each row in the 'reader' variable one at a time.
#     print (row)





# import csv 

# with open("January.csv") as file: 
#   reader = csv.reader(file) 
#   line = 0

#   for row in reader: 
#     print (", ".join(row)) # adds a comma and space and then joins data, you could try joining with tabs too with `\t`








# import csv # Imports the csv library

# with open("January.csv") as file: 
#   reader = csv.DictReader(file) # Treats the file as a dictionary 
#   line = 0
#   for row in reader: 
#     print (row["Net Total"])








# import csv # Imports the csv library

# with open("January.csv") as file: 
#   reader = csv.DictReader(file) # Treats the file as a dictionary 
#   total = 0
#   for row in reader: 
#     print (row["Net Total"])
#     total += float(row["Net Total"]) # Keeps a running total

# print(f"Total: {total}") #Outputs








##### project of day 54

# import csv

# total = 0.0

# with open("Day54Totals.csv") as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     total += float(row["Quantity"]) * float(row["Cost"])

# print(f"Total: ${round(total,2)}")































# import os

# print(os.listdir()) # Lists all the files in the current directory. Useful for checking that a file is in the folder we think it is.

# files = os.listdir()
# if "quickSave.txt" not in files:
#   print("Error: Quick Save not found.")
# #Checks if a file is in a directory and outputs an error if not.





# creating a folder with os library

# import os

# os.mkdir("Hello")



# import os

# os.rename("myname.txt", "NEW.o")




# import os

# filename = os.path.join("Hello/", "aFile.txt")

# f = open(filename, "w")
# f.write("Hi")
# f.close()
















# project of day 55

  # | Name | Date | Priority
# import os, time, random
# todo = []
# fileExists = True
# try:
#   f = open("to.do", "r")
#   todo = eval(f.read())
#   f.close()
# except:
#   fileExists = False

# def add():
#   time.sleep(1)
#   os.system("clear")
#   name = input("Name > ")
#   date = input("Due Date > ")
#   priority = input("Priority > ").capitalize()
#   row = [name, date, priority]
#   todo.append(row)
#   print("Added")

# def view():
#   time.sleep(1)
#   os.system("clear")
#   options = input("1: All\n2: By Priority\n> ")
#   if options=="1":
#     for row in todo:
#       for item in row:
#         print(item, end=" | ")
#       print()
#     print()
#   else:
#     priority = input("What priority? > ").capitalize()
#     for row in todo:
#       if priority in row:
#         for item in row:
#           print(item, end=" | ")
#         print()
#     print()
#   time.sleep(1)

# def edit():
#   time.sleep(1)
#   os.system("clear")
#   find = input("Name of todo to edit > ")
#   found = False
#   for row in todo:
#     if find in row:
#       found = True
#   if not found:
#     print("Couldn't find that")
#     return
#   for row in todo:
#     if find in row:
#       todo.remove(row)
#   name = input("Name > ")
#   date = input("Due Date > ")
#   priority = input("Priority > ").capitalize()
#   row = [name, date, priority]
#   todo.append(row)
#   print("Added")

# def remove():
#   time.sleep(1)
#   os.system("clear")
#   find = input("Name of todo to remove > ")
#   for row in todo:
#     if find in row:
#       todo.remove(row)

# while True:
#   menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
#   if menu == "1":
#     add()
#   elif menu == "2":
#     view()
#   elif menu == "3":
#     edit()
#   else:
#     remove()

#   time.sleep(1)
#   os.system("clear")

#   if fileExists:
#     try:
#       os.mkdir("backups")
#     except:
#       pass
#     name = f"backup{random.randint(1,1000000000)}.txt"
#     os.popen(f"cp to.do backups/{name}")
    
  
#   f = open("to.do", "w")
#   f.write(str(todo))
#   f.close()































# project day 56
# import csv, os

# with open("100MostStreamedSongs.csv") as file:
#   reader = csv.DictReader(file)
  
#   for row in reader:
#     dir = os.listdir()
#     artist = row["Artist(s)"].title()
#     print(artist)
#     if artist not in dir:
#       os.mkdir(artist)
#     song = row["Song"]
#     print(row["Song"])
#     path = os.path.join(f"{artist}/", song)
#     f = open(path, "w")
#     f.close()
















# def reverse(value):
#   if value <= 0:
#     print("Done!")
#     return
#   else:
#     for i in range(value):
#       print("💯", end="|")
#     print()
#     reverse(value - 1)
# reverse(15)






# project day 57

# print("🌟Factorial Finder🌟")

# def factorial(value):
#   if value == 1:
#     return 1
#   else:
#     return value * factorial(value-1)

# print(factorial(3))





































# for i in range(5):
#   print(i)



# import random

# colors = ["Red","Orange", "Yellow", "Green", "Teal", "Blue", "Purple", "Violet"]

# while True:
#   menu = input("1:Color or 2: exit?\n =>")

#   if menu =="1":
#     print(random.choice(colors))
#   else:
#     break










# import random, os, time
# totalAttempts = 0

# def game():
#   attempts = 0
#   number = random.randint(1,100)
#   while True:
#     guess = int(input("Pick a number between 1 and 100: "))
#     if guess > number:
#       print("Too high")
#       attempts+=1
#     elif guess < number:
#       print("Too low")
#       attempts+=1
#     else:
#       print("Just right!")
#       print(f"{attempts} attempts this round")
#       return attempts

# while True:
#   menu = int(input("1: Guess the random number game\n2: Total Score\n3: Exit\n> "))
#   if menu == 1:
#     totalAttempts+= game()
#   elif menu == 2:
#     print(f"You've had {totalAttempts} attempts")
#   else:
#     break



















# palindrome
# def palindrome(word):
#   if len(word)<=1:
#     return True
#   if word[0] != word[-1]:
#     return False
#   return palindrome(word[1:-1])

# print(palindrome("madam"))



































## time


import datetime

# myDate = datetime.date(year=2006, month=4, day= 23)

# print(myDate)

# # This code outputs '2022-12-07'



# today = datetime.date.today()
# print(today)
# # This code outputs the current date from your computer's clock.



# day = int(input("Day: "))
# month = int(input("Month: "))
# year = int(input("Year: "))

# date = datetime.date(year, month, day)
# print(date)






# # Delta Force

# today = datetime.date.today() # Today's date

# difference = datetime.timedelta(days=14) # The difference I want

# newDate = today + difference # Add today to the delta difference to see the date in 14 days time.

# print(newDate)








# today = datetime.date.today() # Today's date

# holiday = datetime.date(year = 2024, month = 7, day = 14) # The date of my holiday

# if holiday > today: # If my holiday is in the future
#   print("Coming soon")
# elif holiday < today: #If my holiday date has passed
#   print("Hope you enjoyed it")
# else: # If my holiday date is today
#   print("HOLIDAY TIME!")














# project 60

# today = datetime.date.today()
# print()

# print("✨Event countdown✨")
# day = int(input("Input the day? => "))
# month = int(input("Input the month? => "))
# year = int(input("Input the year? => "))

# date = datetime.date(year, month, day)
# ago = today - date
# if date < today:
#   print(f"😫😫You missed it, it was {ago} days ago😫😫")
# elif date > today:
#   print("😎COMMING SOON!!😎")
# else:
#   print("🎉🎉🎈🎈Today!!🎈🎈🎉🎉")






# today = datetime.date.today()

# print("EVENT COUNTDOWN")
# day = int(input("Day: "))
# month = int(input("Month: "))
# year = int(input("Year: "))
# event = datetime.date(year, month, day)

# difference = event - today
# difference = difference.days

# if difference>0:
#   print(f"{difference} days to go")
# elif difference<0:
#   print(f"😭😭😭😭😭😭😭 You missed it by {difference} days!")
  
# else:
#   print("🥳🥳🥳🥳🥳🥳🥳 Today!")

































# db["Ernest"] = {"username": "Escobarb", "password":"2006"}

# keys = db.keys()
# print(keys)

# value = db["Ernest"]
# print(value["username"])






# keys = db.keys()
# for key in keys:
#   print(f"""{key}: {db[key]}""")





# import datetime, os, time

# def addTweet():
#   tweet = input("🐥 > ")
#   timestamp = datetime.datetime.now()
#   key = f"mes{timestamp}"
#   db[key] = tweet
#   time.sleep(1)
#   os.system("clear")

# def viewTweet():
#   matches = db.prefix("mes")
#   matches = matches[::-1]
#   counter = 0
#   for i in matches:
#     print(db[i])
#     print()
#     time.sleep(0.3)
#     counter+=1
#     if(counter%10==0):
#       carryOn = input("Next 10?: ")
#       if(carryOn.lower()=="no"):
#         break
#   time.sleep(1)
#   os.system("clear")


# while True:
#   print("Tweeter")
#   menu = input("1: Add Tweet\n2: View Tweets\n> ")
#   if menu == "1":
#     addTweet()
#   else:
#     viewTweet()















# CLASS ########


# class animal:
#   species = None
#   name = None
#   sound = None
 
#   def __init__(self, name, species, sound, color): # Include the 'self' in the 'init'
#     self.name = name
#     self.species = species
#     self.sound = sound
#     self.color = color

# class bird(animal):

#  def __init__(self):
#     self.name = "Bird"
#     self.species = "Avian"
#     self.sound = "Tweet"
#     self.color = "green"


# cow = animal("Ermintrude", "Bo Taurus", "Moo", "black")
# print(cow.sound)





# class animal:
#   species = None
#   name = None
#   sound = None

#   def __init__(self, name, species, sound):
#     self.name = name
#     self.species = species
#     self.sound = sound


# dog = animal("Dog", "Canine", "Woof")
# print(dog.name)

# cow = animal("Ermintrude", "Bo Taurus", "Moo")
# print(cow.species)

# rabbit = animal("Chinchilar", "angular", "Mee")
# print(rabbit.sound)







# class animal:
#   species = None
#   name = None
#   sound = None
#   # Sets the characteristics

#   def __init__(self, name, species, sound):
#     self.name = name
#     self.species = species
#     self.sound = sound

#   def talk(self):
#     print((f"{self.name} says {self.sound}")) 
#   # 'self' means 'use the identifier given to the object that is accessing this method'. So If I use it with dog it will become 'dog.talk()' etc.

# dog = animal("Brian", "Canine", "Woof")
# dog.talk()

# cow = animal("Ermintrude", "Bo Taurus", "Moo")
# cow.talk()











# class animal:
#   species = None
#   name = None
#   sound = None
#   # Sets the characteristics

#   def __init__(self, name, species, sound):
#     self.name = name
#     self.species = species
#     self.sound = sound

#   def talk(self):
#     print((f"{self.name} says {self.sound}")) 
  # 'self' means 'use the identifier given to the object that is accessing this method'. So If I use it with dog it will become 'dog.talk()' etc.


# class bird(animal):

#   color = None

#   def __init__(self, color):
#     self.name = "Bird"
#     self.species = "Avian"
#     self.sound = "Tweet"
#     self.color = color

# dog = animal("Brian", "Canine", "Woof")
# dog.talk()

# cow = animal("Ermintrude", "Bo Taurus", "Moo")
# cow.talk()

# polly = bird("Green") 
# polly.talk()
# print(polly.color)




# ## project of day 62


# class job:
#   name = None
#   salary = None
#   hoursWorked = None

#   def __init__(self, name, salary, hoursWorked):
#     self.name = name
#     self.salary = salary
#     self.hoursWorked = hoursWorked

#   def print(self):
#     print("== JOB ==")
#     print()
#     print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")

# class doctor(job):
#   experience = None
#   speciality = None

#   def __init__(self, salary, hoursWorked, experience, speciality):
#     self.name = "Doctor"
#     self.salary = salary
#     self.hoursWorked = hoursWorked
#     self.experience = experience
#     self.speciality = speciality

#   def print(self):
#     print("== JOB ==")
#     print()
#     print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
#     print(f"{self.experience:<10} {self.speciality:>21}")

# class teacher(job):
#   subject = None
#   position = None

#   def __init__(self, salary, hoursWorked, subject,  position):
#     self.name = "Teacher"
#     self.hoursWorked = hoursWorked
#     self.salary = salary
#     self.subject = subject
#     self.position = position
  
#   def print(self):
#     print("== JOB ==")
#     print()
#     print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
#     print(f"{self.subject:<10} {self.position:>21}")

# lawyer = job("Lawyer", "$100,000", "40")
# lawyer.print()

# doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
# doc.print()

# teach = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
# teach.print()










###########  project


# class character:
#   name = None
#   health = 100
#   mp = 100

#   def __init__(self, name):
#     self.name = name

#   def print(self):
#     print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}")

#   def setStats(self, health, mp):
#     self.health = health
#     self.mp = mp

# class player(character):
#   nickname = None
#   lives = 3

#   def __init__(self, nickname):
#     self.name = "Player"
#     self.nickname = nickname

#   def print(self):
#     print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tNickname: {self.nickname}\tLives: {self.lives}")

#   def isAlive(self):
#     if self.lives > 0:
#       print(f"{self.nickname} lives on!")
#       return True
#     else:
#       print(f"{self.nickname} has expired!")
#       return False

# ian = player("Ian the mighty")
# ian.print()
# print(ian.isAlive())

# class enemy(character):
#   type = None
#   strength = None

#   def __init__(self, name, type, strength):
#     self.name = name
#     self.type = type
#     self.strength = strength

#   def print(self):
#     print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}")

# class orc(enemy):
#   speed = None

#   def __init__(self, speed):
#     self.name = "Orc"
#     self.type = "Orc"
#     self.strength = 200
#     self.speed = speed

#   def print(self):
#     print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tSpeed: {self.speed}")

# sharron = orc(250)
# gary = orc(205)

# sharron.print()
# gary.print()

# class vampire(enemy):
#   day = True

#   def __init__(self, day):
#     self.name = "Vampire"
#     self.type = "Vampire"
#     self.strength = 150
#     self.day = day

#   def print(self):
#     print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tDay: {self.day}")

# eric = vampire(False)
# eric.print()