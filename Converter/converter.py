import PySimpleGUI as  sg

user_input = 0

#miles to kilometers
def mil_to_kil(miles):
    res = user_input * 1.609
    return res

#kilos to miles
def kil_to_mil(kil):
    res = user_input / 1.609
    return res

 #farenheit to celsius
def fah_to_cel(fah):
    res = user_input * 5/9 - 32
    return res

#celsius to fahrenheit
def cel_to_fah(cel):
    res = user_input * 9/5 + 32
    return res

#pounds to kilos
def pou_to_kil(pou):
    res = user_input * 2.204
    return res

#def 
def kil_to_pou(kil):
    res = user_input / 2.204
    return res

sg.set_options(icon=r"C:\Users\user\downlaods\unit-converter-65.ico",background_color='#fdfdff', element_background_color='#edeeef',text_color='black',text_element_background_color='#fdfdff')
layout = [[sg.Text('Unit Converter', font='Lucinda 20',size=(20,1))],
        [sg.Text('Choose Unit',size=(15,1), font='Lucinda 16'), sg.Combo(['Miles to Kilometeres', 'Kilometers to Miles',
                                                                        'Fahrenheit to Celsius', 'Celsius to Fahrenehit', 
                                                                        'Pounds to Kilos', 'Kilos to Pounds'],
                                                                        key='COMBO', font='Lucinda 16', size=(20,1))],
        [sg.Text('Enter Value', size=(15,1), font='Lucinda 16'),sg.InputText(key='INPUT', font='Lucinda 16',size=(20,1))],
        [sg.Text('Result',font='Lucinda 16',size=(15,1)),sg.Text(key='OUTPUT',font='Lucinda 16',size=(20,1))],
        [sg.Button('Calculate'),sg.Button('Exit',button_color=('white','#D33F49'))]]
window = sg.Window('Converter',layout)
event,values = window.read()






