available = ['lettuce', 'tomatoes','celery','onions','spinach']
unavailable = ['carrots', 'zucchini']


print("Available products: ")
for a in available:
    print(a)
    
print("Unavailable products: ")
for u in unavailable:
    print(u)
while True:
    try:
        menu = int(input("What would you like to do?\n [1] Move to unavailable\n[2] Move to available? \n[3] Exit\n"))
    except ValueError:
        print("Invalid Entry: Please type 1,2 or 3. ")
    else:
        if menu == 1:
            while True:
                #?try: 
                    a_produce = input("Please enter an item from the available products: ").lower().strip()
                #?except ValueError:
                    print("Invalid Entry. Not on list.")
                else:
                    if a_produce in available:
                        unavailable.append(a_produce)
                        available.remove(a_produce)
                        print(available)
                        print(unavailable)
                    else:
                        print("Invalid selection. Please choose a listed item. ")
                again = input("Would you like to add another item? Y/N: ").capitalize().strip()
                if again == 'Y':
                    continue
                else:
                    break
        elif menu == 2:
            while True:
                u_produce = input("Please enter an item from the unavailbe products: ")
                if u_produce in unavailable:
                    available.append(u_produce)
                    unavailable.remove(u_produce)
                    print(available)
                    print(unavailable)
                else:
                    print("Invalid selection. Please choose an item from the unavailble list: ")
                again = input("Would you like to add another item? Y/N: ").capitalize().strip()
                if again == 'Y':
                    continue
                else:
                    break
        elif menu == 3:
            print("Goodbye")
            break
        else: 
            print("This is an incorrect selection. Please choose 1 or 2.")      
