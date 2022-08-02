#gamplay function 4 options [1] buy, sell, withdrawal, exit
#menu should be a def

#Class Farm
#
# active = True
# while active:
#     try:
#         gameplay = input("[1] Buy seeds\n[2] Sell Harvest\n[3] Withdrawal\n[4] Exit\n").strip()
#     except ValueError:
#         print("Invalid entry. Try selecting a numer 1 to 4")
#    

#6 parameters = melon_seeds, pumpkin_seeds, wheat_seeds, melon, pumpkin, wheat
    #melon, pumpkin, wheat = harvest
#7 methods 
    # buy_wheat_seeds() 1. purchase = 10 seeds 
    #2. purchase subtracts 10 from cash
    #3. 50 seeds must be sold before they can be converted to harvest

    #buy_melon_seeds() 1. purchase = 10 seeds
    # purchase subracts 15 cash
    #50 seeds must be sold before they can be converted to harvest

    #buy_pumpkin_seeds() 1. purchse = 10 seeds
    #2. purchase subtracts 20 from cash
    #350 seeds must be sold before they can be converted to harvest

    #sell_wheat() multiply all seeds by 1.2 and convert to cash 
    #sell melon() multiply all seeds by 1.5 and convert to cash
    #sell pumpkin() multiply all seds by 1.8 and convert to cash
    #withdrawal() user withdraws amount from bank and turns it into cash

#starting cash 100$ bank = $200
#table with (is this a list or a dictionary?) updates each action so that the user 
    #tracks how many seeds have been sold
    #how many seeds have been purchased
    #How many seeds are needed until harvest
    #how much cash is available
    #how much money in the bank

from termcolor import colored

class Farm:
    #include params in the init

    def __init__(self,melon_seeds=0,pumpkin_seeds=0,wheat_seeds=0,melon=0, pumpkin=0, wheat=0,cash=100,bank=200):
        self.melon_seeds = melon_seeds
        self.pumpkin_seeds = pumpkin_seeds
        self.wheat_seeds = wheat_seeds
        self.melon = melon
        self.pumpkin = pumpkin
        self.wheat = wheat
        self.cash = cash
        self.bank = bank

    def menu(self):
        print(f'''CAPITAL\t\t SEED BANK\t\t Harvest
        --------------------------------------------------------------------------------------
        Cash ${self.cash}\t\tWheat seeds: {self.wheat_seeds}\t\t Harvest Wheat: {self.wheat}
        Bank: ${self.bank}\t\tMelon Seeds: {self.melon_seeds}\t\t Harvested Melon: {self.melon}
                                Pumpkin Seeds:{self.pumpkin_seeds}\t\t Harvested Pumpkin: {self.pumpkin}''')
#cash formatting - correct
    def buy_wheat_seeds(self):#has to have self because its associatied with farm object
        self.wheat_seeds += 10
        self.cash -= 10
        if self.wheat_seeds == 50:
            self.wheat = 50
            self.wheat_seeds = 0
        print("Congrats! You have purchased new wheat harvest!")

    def buy_melon_seeds(self):
        self.melon_seeds += 10
        self.cash -= 15
        if self.melon_seeds == 50:
            self.melon = 50
            self.melon_seeds = 0
        print("Congrats! You have purchased new melon harest!")
    
    def buy_pumpkin_seeds(self):
        self.pumpkin_seeds += 10
        self.cash -= 20
        if self.pumpkin_seeds == 50:
            self.pumpkin = 50
            self.pumpkin_seeds = 0
        print("Congrats! You have purchased new pumpkin harvest!")
    
    def sell_wheat(self):
        if self.wheat < 50:
            print(colored("Not enough harvest to sell",'red'))
        else:
            if self.wheat %50 == 0:
                self.cash += self.wheat*1.2
                self.wheat = 0
                print(colored("You have sold your wheat!",'green'))
       
    def sell_melon(self):
        if self.melon < 50:
            print(colored("Not enough havest to sell",'red'))
        else:
            if self.melon %50 == 0:
                self.cash += self.melon*1.5
                self.melon = 0
                print(colored("You have sold your melon!",'green'))
    
    def sell_pumpkin(self):
        if self.pumpkin < 50:
            print(colored("Not enough harvest to sell",'red'))
        else:
            if self.pumpkin > 0:
                self.pumpkin %50 == 0
                self.cash += self.pumpkin*1.8
                self.melon = 0
                print(colored("You have sold your pumpkin!",'green'))

    def withdraw(self):
        withdrawal_choice = int(input("How much cash would you like to withdraw? \n"))
        print(withdrawal_choice)
        if self.bank > 0:
            self.bank -= withdrawal_choice
            self.cash += withdrawal_choice
            print("You have made a withdrawal")
        elif self.bank < withdrawal_choice:
            print("Sorry you don't have enough to withdrawal that much. Please check your blance. ")
        elif self.bank == 0:
            print("Sorry, you don't have the funds to withdrawal. You have a 0 balance")
        else:
            print("Invalid entry. Try again!")

farm_object = Farm()

def main():
    farm_object.menu()
    active = True
    while True:
        choice = int(input("Welcome to the farm! What would you like to do?\n[1] Withdrawal\n[2] Sell Harvest\n[3] Buy Seeds\n[4] Exit\n"))
        if choice == 1:
            while True:
                #withdrawal_choice = int(input("How much cash would you like to withdraw? \n"))
                #should this be a return? 
                #if withdrawal_choice >= 1: #where does this w/d choice go!?!?
                    farm_object.withdraw()
                    farm_object.menu()
                    withdrawal2 = int(input("Would you like to \n[1] Make another withdrawal\n[2] Return to the main menu\n "))
                    if withdrawal2 == 1:
                        continue
                    elif withdrawal2 == 2:
                        break
                    else:
                        print("Invalid Entry. Try selcting 1 or 2. ")

        elif choice == 2:
            while True:
                #need to write code that identifies if there is harvest to sell
                #try
                sell_harvest_choice = int(input("what type of harvest would you like to sell?\n[1] Wheat\n[2] Melon\n[3] Pumpkin\n[4] Main Menu\n"))
                #except ValueError:
                if sell_harvest_choice == 1:
                    farm_object.sell_wheat()
                    farm_object.menu()
                    #print("You sold wheat!")
                elif sell_harvest_choice == 2:
                    farm_object.sell_melon()
                    farm_object.menu()
                    #print("You sold melon")
                elif sell_harvest_choice == 3:
                    farm_object.sell_pumpkin()
                    farm_object.menu()
                elif sell_harvest_choice == 4:
                    farm_object.menu()
                    break
                else:
                    print("Invalid Entry. Please select options 1-4")
            print("You chose sell harvest")
            pass
        elif choice == 3:
            while True:
                buy_seeds_choice = int(input("What type of seed would you like to purchase?\n[1] Wheat Seeds\n[2] Melon Seeds\n[3] Pumpkin Seeds\n[4] Back to the main menu\n"))
                if buy_seeds_choice == 1:
                    farm_object.buy_wheat_seeds()
                    farm_object.menu()
                elif buy_seeds_choice == 2:
                    farm_object.buy_melon_seeds()
                    farm_object.menu()
                elif buy_seeds_choice == 3:
                    farm_object.buy_pumpkin_seeds()
                    farm_object.menu()
                else:
                    break
        elif choice == 4:
            farm_object.menu()
            print("Good bye")
            break
        else:
            print("incorrect selection. choose 1 to 4")
main()