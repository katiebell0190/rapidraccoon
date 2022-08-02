import PySimpleGUI as sg
from matplotlib.ft2font import LOAD_VERTICAL_LAYOUT
from nbformat import read
from sympy import cancel

#PopUPS
#sg.popup("Alert!!")
#sg.popup_yes_no("Are you okay?")
# sg.popup_cancel("are you sure you want to cancel?")
# sg.popup_ok_cancel("you want to cancel?")
# sg.popup_error("you messed up?")
# sg.popup_timed("Closing in 3,2,1...")
# sg.popup_auto_close("Closing...")

#Basic Window 1 - (ONE-SHOT WINDOW)
# layout = [[sg.Text('Enter a number')],
#         [sg.Input()],
#         [sg.OK()]]
# window = sg.Window('My first window',layout=layout)
# event,values=window.read()
# window.close()

# sg.popup(event,values[0])

# #Basic WINDOW 2 - (ONE SHOT WINDOW)
# layout = [[sg.Text("ONe-Shot Window 2")],
#           [sg.Text("Enter something here"),sg.Input(key='IN')],
#           [sg.Submit(),sg.Cancel()]]
# window = sg.Window("One-Shot WIndeow2",layout)
# events,values = window.read()
# window.close()

# sg.popup("You entered: ",values['IN'])

# layout = [[sg.Text('Filename')],
#             [sg.Input(), sg.FileBrowse()],
#             [sg.OK(), sg.Cancel()]]
# window = sg.Window('Get File',layout)
# event,values = window.read()
# window.close()

# sg.popup(event,values[0])

# #BASIC WINDOW 3 - PERSISTENT WINDOW
# layout = [[sg.Text("Persistent Window")],
#             [sg.Input()],
#             [sg.Button('Print'),sg.Exit()]]
# window = sg.Window("This window stays open",layout)

# while True:
#     event,values = window.read()
#     if event == 'Exit' or event == sg.WIN_CLOSED:
#         break
#     else:
#         print(event,values)

#BASIC WINDOW 4 - RETURN VALUES 

# layout = [[sg.Text("ENTER YOUR INFO")],
#             [sg.Text('Name',size=(7,1)),sg.InputText(key='NAME')],
#             [sg.Text('Address',size=(7,1)),sg.InputText(keys='Address')],
#             [sg.Text('Phone',size=(7,1)),sg.InputText(keys='PHONE')],
#             [sg.Submit(),sg.Cancel()]]
# window = sg.Window('Data Entry',layout)
# event,values = window.read()
# window.close()

# sg.popup(event,values['NAME'],values['ADDRESS'],values['PHONE'])

# #BASIC WINDOW 5 (RETURN VALUES ONTO WINDOW ITSELF)
# layout = [[sg.Text('Enter something'),sg.InputText(key='IN',size=(20,1))],
#         [sg.Text('',size=(12,1)),sg.Text(key='OUT',background_color='#FFFFFF',size=(20,1))],
#         [sg.Button('OK'),sg.Button('Exit')]]
# window = sg.Window('Return onto self', layout)
# while True:
#     event,values = window.read()
#     if event == 'Exit' or event == sg.WIN_CLOSED:
#         break
#     else:
#         window['OUT'].update(values['IN'])
#     window.close()

# layout = [[sg.Text('Email'),sg.InputText(key='EMAIL',size=(20,1))],
#             [sg.Text('Phone number'),sg.InputText(key='PHONE',size=(13,1))],
#             [sg.Submit(),sg.Cancel()]]
# window = sg.Window('Data Entry',layout)
# event,values = window.read()
# window.close()
# sg.popup(event,values['EMAIL'],values['PHONE'])

# #Simple form
# layout = [[sg.Text('Your information',font='Arial 20')],
#             [sg.Text('First Name',size=(10,1),font='Arial 14'), sg.InputText(key='FNAME',font='Arial 14',size=(15,1),password_char='*')],
#             [sg.Text('Last name',size=(10,1),font='Arial 14'), sg.InputText(key='LNAME',font='Arial 14',size=(15,1))],
#             [sg.Text('Email',size=(10,1),font='Arial 14'), sg.InputText(key='EMAIL',font='Arial 14',size=(15,1))],
#             [sg.Submit(font='Arial 14'),sg.Cancel(font='Arial 14')]]
# window = sg.Window('Sign up',layout)
# while True:
#         event,values = window.read()
#         if event == 'cancel' or event == sg.WIN_CLOSED:
#             break
#         elif event == 'Submit':
#             if values['FNAME'] == '' or values['LNAME'] == '' or values['EMAIL'] == '':
#                 sg.popup_error('Input needed',font='Arial 14')
#             elif values['FNAME'].isdigit() or values['LNAME'].isdigit() or values ['EMAIL'].isdigit():
#                 sg.popup_error('Digits not alowed',font='Arial 14')
#             elif values['FNAME'.isspace()] or values ['LNAME'].isspace() or values['EMAIL'].isspace():
#                 sg.popup_error('Invalid input',font='Arial 14')
#             elif '@' not in values['EMAIL']:
#                 sg.popup_errr("Not a valid email")
#             else:
#                 print(f"Name: {values['FNAME'].capitalize()} {values['LNAME'].capitalize()}")
#                 print(f"Email: {values['EMAIL']}")
#                 window.close()
# sg.popup_timed('Submitted Successfully!',font='Arial 14')


# sg.theme('DefaultNoMoreNagging')
# layout = [[sg.Text('Full Name'), sg.InputText(key='NAME')],
#             [sg.Text('Gender'),sg.Radio('Male',1, key='MALE'),sg.Radio('Female',1,key='FEMALE')],
#             [sg.Text('Comments'),sg.Multiline(key='COMMENT',size=(44,10))],
#             [sg.Submit(),sg.Cancel()]]

# window = sg.Window("Comments Form",layout)
# event,values = window_read()

# while True:
#     event,values = window.read()
#     if event == 'Cancel' or event == sg.WIN_CLOSED:
#         break
#     elif event == 'Submit':
#         sg.popup('Values entered: ',values['NAME'],'Male' if values['MALE'] else ['Female'], values['COMMENT'])
# window.close()

sg.theme('BluePurple')
layout = [[sg.Text('Username'), sg.InputText(key='LOGIN',font='Arial 14', size=(12,1))],
            [sg.Text('Password'), sg.InputText(key='PASSWORD',font='Arial 14', size=(12,1), password_char='*')],
            [sg.Submit(),sg.Cancel()]]

window = sg.Window("Login",layout)

while True:
    event,values = window.read()
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        break
    elif event == 'Submit':
        sg.popup('Values entered: ',values['LOGIN'],values['PASSWORD'])
    else:
        print("You have successfully logged in!")
window.close()

#two functions
#1. Create account
#2. Log in account on a guiy