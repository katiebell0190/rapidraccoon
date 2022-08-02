from ast import While
from prj_connect import connect
from prj_fetchone import fetch_one
from prj_fetchall import view_report_all
from prj_print_csv_file import print_csv_file
from prj_send_email import sendemail
#from prj_close_connection

#inforce_object = Report()

def main_two():
    while True:
        active = True
        try:
            choice = int(input("Welcome to the Inforce Report App! \nSelect an option: \n[1] Connect to database \n[2] View Sample Record \n[3] View all records \n[4] Export to CSV file \n[4] Email CSV file \n[5]View Report \n[6] Exit\n"))
            if choice == 1:
                connect()
            elif choice == 2:
                fetch_one()
            elif choice == 3:
                view_report_all()
            elif choice == 4:
                print_csv_file()
            elif choice == 5:
                sendemail()
            #elif choice == 6:
                #exit
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid Input.")
        else:
            if choice == 0:
                raise ValueError("Zero not allowed")
            print(choice)
            break
main_two()
    





