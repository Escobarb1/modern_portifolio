# Dictionaries

# myUser = {"name": "David", "age": 128}
# print(myUser["age"])

# myUser = {"name": "David", "age": 128}

# myUser["name"] = "The legendary David"
# print(myUser)

# # This code outputs 'name:'the legendary David', 'age':'128.


# myUser = {"name":"Andy", "age":128, "age":129}

# print(myUser["name"])





# building a contact card

# print("🌟Contact Card🌟")
# print()
# name = input("Input your name: ").capitalize().strip()
# date0fBirth = input("Input your of date of birth: ").strip()
# telephone = input("Input your telephone number: ").strip()
# email = input("Input your email: ")
# address = input("Input your address: ")
# contactCard = {"name": name, "date of birth": date0fBirth, "telephone": telephone, "email": email, "address": address}

# print()
# print(f"""Hi {contactCard["name"]}. Our dictionary says that you were
# born on {contactCard["date of birth"]}, we can call you on {contactCard["telephone"]},
# email {contactCard["email"]}, or write to {contactCard["address"]}.""")









# print("🌟Contact Card🌟")
# print()
# name = input("Input your name: ").capitalize().strip()
# date0fBirth = input("Input your of date of birth: ").strip()
# telephone = input("Input your telephone number: ").strip()
# email = input("Input your email: ")
# address = input("Input your address: ")
# contactCard = {"name": name, "date of birth": date0fBirth, "telephone": telephone, "email": email, "address": address}

# print()
# print(f"""Name: {contactCard["name"]}""")
# print(f"""Date of birth: {contactCard["date of birth"]}""")
# print(f"""telephone: {contactCard["telephone"]}""")
# print(f"""email: {contactCard["email"]}""")
# print(f"""address: {contactCard["address"]}""")





# Dictionaries with loops

# myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

# for value in myDictionary.values():
#   print(value)

  # or

# myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

# for i in myDictionary:
#   print(myDictionary[i])




# myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

# for name,value in myDictionary.items():
#   print(f"{name}:{value}")








###project

# print("🌟Website Rating🌟")
# print()
# website = {"name": None, "url": None, "description": None, "rating": None}

# for name in website.keys():
#   website[name] = input(f"{name}: ")

# print()
# for name, value in website.items():
#   print(f"{name}: {value}")











# print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
# print()
# mokedex = {"Beast name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

# print("MokéBeast")
# print()
# for name, value in mokedex.items():
#   mokedex[name] = input(f"{name}:\t").strip().title()
# if mokedex["Type"]=="Earth":
#   print("\033[32m", end="")
# elif mokedex["Type"]=="Air":
#   print("\033[37m", end="")
# elif mokedex["Type"]=="Fire":
#   print("\033[31m", end="")
# elif mokedex["Type"]=="Water":
#   print("\033[34m", end="")
# else:
#   print("\033[33m", end="")
# for name, value in mokedex.items():
#   print(f"{name:<15}: {value}")


























# list in deeper dimension

# my2DList = [ ["Johnny", 21, "Mac"],
#              ["Sian", 19, "PC"],
#              ["Gethin", 17, "PC"] ]
# my2DList[1][2] = "Linux"
# print(my2DList)
# for i in my2DList:
#   print(i)

























# project
# import random

# print("🐕Bingo Card🐕")
# print()
# bingo = []

# def ran():
#   number = random.randint(1,90)
#   return number


# def prettyPrint():
#   for row in bingo:
#     print(row)


# numbers = []
# for i in range(8):
#   numbers.append(ran())

# numbers.sort()

# bingo = [ [ numbers[0], numbers[1], numbers[2]],
#           [ numbers[3], "BINGO", numbers[4] ],
#           [ numbers [5], numbers[6], numbers[7]]
#         ]
# prettyPrint()




# listOfShame = [] 
# # Creates an empty list.

# while True: 
#   # Starts a never ending loop (until we end it)
#   name = input("What is your name?\n => ")
#   age = input("What is your age?\n => ")
#   pref = input("What is your computer platform?\n => ")
#   # Get the user input.

#   row = [name, age, pref] 
#   # Assigns the 3 variables into a single row.

#   listOfShame.append(row) 
#   # Adds the contents of the row variable at the end of the list

#   exit = input("Exit? y/n\n => ") 
#   # Get user choice to quit, yes or no?

#   if (exit.strip().lower()[0] == "y"): 
#     # strip removes unwanted spaces from the input. lower()[0] makes sure the first character of the input is lower case so it can be compared to 'y'
#     break # break ends a loop and jumps to the next line of code that is not part of the loop.
    
# print(listOfShame) # Outputs the list. Note this is NOT part of the loop (not indented), it only runs once the loop ends.







# listOfShame = [] 

# def prettyPrint():
#   print()
#   for row in listOfShame:
#     for item in row:
#       print(f"{item:^20}", end=" | ")
#     print()
#   print()

# while True: 
#   name = input("What is your name? ")
#   age = input("What is your age? ")
#   pref = input("What is your computer platform? ")
  
#   row = [name, age, pref] 

#   listOfShame.append(row) 

#   exit = input("Exit? y/n") 

#   if (exit.strip().lower()[0] == "y"):
#     break 

# prettyPrint() 









# import random, os, time

# bingo = []

# def ran():
#   number = random.randint(1,90)
#   return number

# def prettyPrint():
#   for row in bingo:
#     for item in row:
#       print(item, end="\t|\t")
#     print()

# def createCard():
#   global bingo
#   numbers = []
#   for i in range(8):
#     num = ran()
#     while num in numbers:
#       num = ran()
#     numbers.append(ran())
  
#   numbers.sort()
  
#   bingo = [ [ numbers[0], numbers[1], numbers[2]],
#             [ numbers[3], "BG", numbers[4] ],
#             [ numbers [5], numbers[6], numbers[7]]
#           ]

# createCard()
# while True:
#   prettyPrint()
#   num = int(input("Next Number: "))
#   for row in range(3):
#     for item in range(3):
#       if bingo[row][item] == num:
#         bingo[row][item] = "X"

#   exes = 0
#   for row in bingo:
#     for item in row:
#       if item=="X":
#         exes+=1

#   if exes == 8:
#     print("You have won")
#     break

#   time.sleep(1)
#   os.system("clear")
































# project
# import os, time
# todo = []

# def add():
#   time.sleep(2)
#   os.system("clear")
#   name = input("Name? => ")
#   date = input("Due Date => ")
#   priority = input("Prority => ").capitalize()
#   row = [name, date, priority]
#   todo.append(row)
#   print("Added!")


# def view():
#   time.sleep(2)
#   os.system("clear")
#   options = input("View \n 1: View All \n 2: View Priority \n => ")
#   if options == "1":
#     for row in todo:
#       for item in row:
#         print(item, end=" | ")
#       print()
#     print()
#   else:
#     priority = input("What is your priority?\n => ").capitalize()
#     for row in todo:
#       if priority in row:
#         print(item, end=" | ")
#       print()
#     print()
#   time.sleep(2)


# def remove():
#   time.sleep(2)
#   os.system("clear")
#   options = input("What would you like to remove?\n => ")
#   for row in todo:
#     if options in row:
#       todo.remove(row)


# def edit():
#   time.sleep(2)
#   os.system("clear")
#   options = input("Name of todo to edit\n => ")
#   found = False
#   for row in todo:
#     if options in row:
#       found = True
#   if not options:
#     print("Couldn't find that")
#     return
#   for row in todo:
#     if options in row:
#       todo.remove(row)
#   name = input("Name > ")
#   date = input("Due Date > ")
#   priority = input("Priority > ").capitalize()
#   row = [name, date, priority]
#   todo.append(row)
#   print("Added")


# print("TODO List Management System")
# print()
# while True:
  # menu = input("Do you want to \n 1: Add\n 2: View\n 3: Remove \n 4: Edit\n => ")
#   if menu == "1":
#     add()
#   elif menu == "2":
#     view()
#   elif menu == "3":
#     remove()
#   else:
#     remove()

#   time.sleep(1)
#   os.system("clear")










































# clue = {}
# def prettyPrint():
#   print()
  
#   for key, value in clue.items():
#     # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
#     print(key, end=": ")
#     for subKey, subValue in value.items():
#       # (nested) `for` loop moves along every subkey and subvalue in each subDictionary.
#       print(subKey, subValue, end=" | ")
#     print()
    
# while True:
#   name = input("Name: ")
#   location = input("Location: ")
#   weapon = input("Weapon: ")

#   clue[name] = {"location": location, "weapon":weapon} 

#   prettyPrint()





# john = {"daysCompleted": 46, "streak": 22}
# janet = {"daysCompleted": 21, "streak": 21}
# erica = {"daysCompleted": 75, "streak": 6}

# courseProgress = {"John":john, "Janet":janet, "Erica":erica}

# print(courseProgress["Erica"]["daysCompleted"])





# project
# import os, time

# mokedex = {}

# def prettyPrint():
#   print(f"Name\tType\tHP\tMP")
#   for key, value in mokedex.items():
#     print(f"""{key:^1}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")

# while True:
#   print("Add your Beast!")
#   name = input("Name > ").title()
#   type = input("Type > ").title()
#   hp = int(input("HP > "))
#   mp = int(input("MP > "))
#   mokedex[name] = { "type": type, "hp": hp, "mp": mp}
#   print("----------")
#   print()
#   prettyPrint()

























# import os, time, random
# print("-----------")


# trumps = {}
# trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
# trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
# trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
# trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

# while True:
#   print("TOP TRUMPS")
#   print()
#   print("Characters")
#   print()
#   for key in trumps:
#     print(key)
#   print()
#   user = input("Pick your character\n> ")
#   comp = random.choice(list(trumps.keys()))
#   print("Computer has picked", comp)

#   print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")

#   answer = input("> ")

#   print(f"{user}: {trumps[user][answer]}")
#   print(f"{comp}: {trumps[comp][answer]}")

#   if trumps[user][answer] > trumps[comp][answer]:
#     print(user, "wins")
#   elif trumps[user][answer] < trumps[comp][answer]:
#     print(comp, "wins")
#   else:
#     print("Draw")


#   time.sleep(3)
#   os.system("clear")