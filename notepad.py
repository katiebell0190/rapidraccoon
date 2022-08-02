import PySimpleGUI as sg
import os
import sys

sg.set_options()

menu = [['File',['New File','Open File','Save','Save as...']],['Edit',['Undo','Redo']]]
layout = [[sg.Menu(menu,key='MENU',font='Lucinda 12')],
            [sg.Multiline(size=(90,20),key='MULTI',expand_x=True,expand_y=True)]]
window = sg.Window('Python Notepad',layout,return_keyboard_events=True,resizable=True)
event,values = window.read()

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        sys.exit()
    else:
        if event == 'Open File':
            #OPEN FILE
            layout2 = [[sg.Text('Open',font='Lucinda 12')],
                    [sg.Input(key='INPUT',size=(25,1)),sg.FilesBrowse(key='FILE',target='INPUT')],
                    [sg.Ok(font='Lucinda 12',key='Ok'),sg.Exit(key='EXIT',font='Lucinda 12')]]
            browse_window = sg.Window('File Browse',layout2)
            event,value = browse_window.read()

            filename = values['FILE']
            file_name = os.path.join(os.path.dirname(__file__),filename)

            with open(filename,'r') as read_file:
                rf = read_file.read()
            window['MULTI'].update(value=rf)
            browse_window.Disappear()
            window.Reappear()

            if event == 'Save':
                pass
            if event == 'Save as...':
                pass
            window.close
