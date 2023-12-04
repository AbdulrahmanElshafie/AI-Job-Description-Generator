from Bot import Bot
from tqdm import tqdm
import time
import PySimpleGUI as sg


def GUI():
    layout = [[sg.Text("Enter your agency's industry")],
              [sg.InputText()],

              [sg.Text("Enter your agency's name")],
              [sg.InputText()],

              [sg.Text("Add any additional information as inspiration for the program")],
              [sg.InputText()],

              [sg.Submit(), sg.Cancel()]]
    window = sg.Window("HR Assistant - V1.5", layout, size=(300, 200))
    events, values = window.read()

    if events is not None:
        while (bool(values[0] == '') | bool(values[1] == '')) & bool(events == 'Submit'):
            sg.popup('Warning!!', 'Enter the company name and industry')
            events, values = window.read()

    window.close()
    return values, events


company_info, response = GUI()

if response == 'Submit':
    file = open('positions.txt', 'r')
    positions = file.read().split('\n')

    bot = Bot(company_industry=company_info[0], company_name=company_info[1])
    bot.login()

    for i in tqdm(range(len(positions)), desc="Tasks remaining", unit="task", ncols=60,
                  bar_format='{l_bar}{bar}{n_fmt}/{total_fmt}'):

        if len(company_info[2]) == 0:
            bot.prompt(positions[i])
        else:
            bot.prompt(positions[i], company_info[2])

        time.sleep(1)

    print('Task Completed!!')
    bot.quit()
