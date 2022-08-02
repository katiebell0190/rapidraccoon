# from asyncio import events


# x = 0
# while x < 10:
#     x+=1
#     print(x)

# x = 0
# while x < 10:
#     x+=1
#     if x % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# x = 0
# while x < 30:
#     x+=1
#     if x % 3 == 0:
#         print ("skipped")
#     else:
#         print(x)


# username = "caitlin"
# password = "123"
# attempts = 5

# while attempts > 0:
#     attempts -= 1
#     name = input("Enter username: ")
#     pwd = input("Enter password: ")

#     if name == username and password == pwd:
#         print ("welcome to the account!")
#         break
#     else:
#         print("Incorrect. Try again.")
#         print(f"You have {attempts} attempts left.")
#         continue

# import random
# #variables for score
# player_counter = 0
# machine_counter = 0


# print("COIN TOSSER GAME")
# #begin outter loop
# while True:
#     choice = input("[1] Play\n[2] Exit\n ")
# #begin inner loop
#     if choice == '1':
#         while True:
# #print score card with player scores            
#             scorecard = f"Player\t\tMachine\n----------------------\n{player_counter}\t\t{machine_counter}"
# #machine random function
#             machine = random.choice(["Heads","Tails"])
# #Player input
#             player = input("Heads or Tails? ").capitalize().strip()
#             if player == machine:
#                 print("Correct!")
#                 player_counter +=1
#                 print(f"Player: {player_counter}")
#             elif player != machine:
#                 print("Wrong guess!")
#                 machine_counter +=1
#                 print(f"Machine: {machine_counter}")
#             again = input("Play again? Y/N: ").capitalize().strip()
#             if again == Y:
#                 continue
#             else: 
#                 print(scorecard)
# #zero out scorecard
#                 player_counter = 0
#                 machine_counter = 0
#                 break
#     else:
#         print("Buhbye")
#         break

# print("COIN TOSSER GAME")
# player_count = 0
# machine_count = 0
# bouts = 10
# while bouts > 0:
#     bouts -=1
#     machine = random.choice(['Heads','Tails'])
#     player = input("Heads or Tails?").capitalize().strip()

#     if player ==machine:
#         print("Correct!")
#     elif player !=machine:
#         print("Wrong!")


# list2 = ['kale', 'celery']

# print("Add Item to Cart")
# while True:
#     item = input("[1] Add items\n[2] Exit \n")
#     if item == '1':
#         while item == '1':
#             item_input = input("Please enter an item: ")
#             list2.append(item_input)
#             print(list2)
       
#             again = input("Do you want to add another item? Y/N \n").capitalize().strip()
#             print(again)
#             if again == "Y":
#                 continue
#             else:
#                 break

#     elif item =="2":
#         print("Goodbye!")
#         break
#     else:
#         print("Error")
#         break
