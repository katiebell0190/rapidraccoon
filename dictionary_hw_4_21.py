#Assignment 1 - Create a menu
#Create dictionary with fname/lname & username/password
#Give me something to identify you are who you say you are
#1 Forgot username - return username
#2 Reset password
#3 Exit

login_storage = {
    'user1': { 
        'fname': 'caitlin',
        'lname': 'waszgis',
        'username': 'cwaszgis1',
        'password': 'A12345',
    },
    'user2': { 
        'fname': 'shawn',
        'lname': 'bell',
        'username': 'sbell',
        'password': 'B12345',
    },
    'user3': { 
        'fname': 'chris',
        'lname': 'waszgis',
        'username': 'cwaszgis2',
        'password': 'C12345',
    },
        'user4': { 
        'fname': 'bruce',
        'lname': 'lee',
        'username': 'blee',
        'password': 'D12345',
    },

}

#print(login_storage)
#k = login_storage.keys()
#print(k)

#v = login_storage.values()
#print(v)

#kv = login_storage.items()
#print(kv)


v = login_storage.values()
    #print(v)
print("Welcome to the student login verification app. Here are your optoins: [1] Recover login info [2] Exit ")
choice = input("What would you like to do? ")
active = True
while True:
    if choice == '1':
        search = input("Enter the last name of the student you are searching for: ").lower().strip()
        for l in login_storage:
            lname = login_storage[l].get('lname')
            
            if search == lname:
                print("match")
            else:
                print("not a match")
            active = False

        again = input("Check another last name? Y/N ").capitalize().strip()
        if again == 'Y':
            continue
        else:
            break
    elif choice == '2':
        print("Goodbye!")
        break

              #for usr in v:
                #if verify == usr['username']:


