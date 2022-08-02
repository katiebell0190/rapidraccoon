# import getpass
# password = getpass.getpass(prompt="Enter Password.")
# print(password)

#Greeting - For HOMEWORK
print("welcome to NE Animal Services")
print("[1] Adopt a Pet \n[2] Find a lost Pet\n[3] Licencing \n[4] Vaccinations\n[5] Spay and Nueter\n[6] Microchipping")
options = input("Choose an option 1 to 6?: ")
print(options) 

if options == '1':
    print("[1] Adopt a Dog\n[2] Adopt a Cat\n[3] Adopt a Pig")
    choice = input("Choose an option: ")
    if choice == '1':
        print("Dog Lover!")
    elif choice == '2':
        print("Carol Baskins!")
    elif choice == '3':
        print("Piggly wiggly")
    else:
        print("Invalid Option")

elif options == '2':
     print("You chose Find a lost pet. Select the type of pet you lost: [1] dog\n[2] cat\n[3] pig ")
     choice2 = input("Choose an option 1 to 3: ")
     print(choice2)

     if choice2 == '1':
         print("Enter your Dogs name: ")
     elif choice2 == '2':
        print("Enter your Cats name: ")
     elif choice2 == '3':
        print("Enter your Pigs name: ")
     else:
         print("Invalid Entry")
    

elif options == '3':
    print("You Chose Pet Licenseing. Pick a county: [1]Sarpy\n[2] Douglas\n[3] Cass ")
    choice3 = input("Enter option 1 to 3: ")
    print(choice3)
    if choice3 == '1':
        print("You chose Sarpy County!")
    elif choice3 == '2':
        print("You chose Douglas County!")
    elif choice3 == '3':
        print("You chose Cass County!")
    else:
        print("Invalid county name")

elif options == '4':
    print("You chose Vaccnations. Pick a vaccine: [1] Rabies\n[2] Distemper ")
    choice4 = input("Enter options 1 or 2: ")

    if choice4 == '1':
        print("You chose rabies!")
    elif choice4 == '2':
        print("What is distemper?")
    else:
        print("Invalid")

elif options == '5':
    print("You chose spay or nueter. Pick a procedure [1] Spay\n[2] Nueter ")
    choice5 = input("Enter option 1 or 2: ")
    print (choice5)

    if choice5 == '1':
        print("You chose Spay!")
    elif choice5 == '2':
        print("You chose Nueter!")
    else:
        print("Not an opition.")

elif options == '6':
    print("You chose microchipping: [1] Dog\n[2] Cat")
    choice6 = input("what type of animal: ")
    print(choice6)

    if choice6 == '1':
        print("Enter your dogs name: ")
    elif choice6 == '2':
        print ("Enter your cats name: ")
    else:
        print("Invalid entry")


        # county = [County names]
        # if county = 
    # 3. how to license your dog or horse
    # 4. animal vaccinations
    # 5.pay/nueter informaiton
    # 6. microchipping
