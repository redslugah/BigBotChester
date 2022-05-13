#gggtracker crawler by reds
import database
import requests
import sys
from bs4 import BeautifulSoup
import time
import tweet
import warnings
import PySimpleGUI as sg
import threading

#classe feita para salvar as informações de maneira organizada
class posts:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        
#função para fazer a busca pelas informações no site específico e formatar a informação, criando um objeto da classe 'posts' com ela
def read():
    URL = "https://gggtracker.com/rss"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    item = soup.find('item')
    itemTitle = (item.find('title').get_text() + "\n")
    itemLink = (item.find('link').next_sibling + "\n")
    read = posts(itemTitle, itemLink)
    return read

"""
definindo a 1 e a 2 informação como a mesma para começar, já que só irei postar quando tiver informação nova que será
testada na função acima. Após ter os dados das leituras, chamdo a função timeToGo que é o loop de leitura e postagem
loop, o if irá checar se a informação da primeira leitura no site é igual a informação da segunda leitura
caso seja, irá aguardar 180 segundos e ler novamente
caso a informação esteja diferente, significa que o que estou buscando foi atualizado, então pego essa informação diferente
formato ela e chamo meu modulo tweet e sua função tweet (tweet.tweet(second)), passo a informação mais recente para ser postada
e então faço com que as informações fiquem iguais novamente para continuar comparando com futuras alterações
"""
def main():
    # criando thread para poder manter a GUI responsiva
    t = threading.currentThread()
    warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
    print('Monitoring...\n')
    first = read()
    second = read()
    while getattr(t, "do_run", True):
        if (first.title == second.title and first.link == second.link):
            time.sleep(180)
            second = read()
        else:
            tweet.tweet(second)
            first = second
            second = read()
            print('Monitoring...\n')
    print("\nOh my god, they killed Botty... :(\n")

def configFile(values):
    f = open("config.cfg", "w")
    f.write(values[0]+'\n')
    f.write(values[1]+'\n')
    f.write(values[2]+'\n')
    f.write(values[3]+'\n')
    f.write(values[4]+'\n')
    f.write(values[5]+'\n')
    f.write(values[6]+'\n')
    f.write(values[7])
    f.close()

def createDatabaseWindow(host, user, passw, db):
    layout = [[sg.Text('You can create tables, insert, delete and select data from the configured database here.', font ='bold')]
    ,[sg.Multiline(size=(40,20)), sg.Output(size=(40,20), key='queryValue')]
    ,[sg.Button('SUBMIT QUERY', key='submitQuery'), sg.Button('EXIT', key='exitButton')]]
    window = sg.Window('DATABASE MANAGEMENT', layout, modal=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'exitButton'):
            window.close()
            break
        elif event == 'submitQuery':
            window.FindElement('queryValue').Update('')
            connection = database.createDbConnection(host, user, passw, db)
            if values[0].split()[0] == 'SELECT':
                select = database.readQuery(connection, values[0])
                window.FindElement('queryValue').Update(select)
            else:
                database.executeQuery(connection, values[0])

def configWindow():
    try:
        f = open("config.cfg", "r")
        data = f.read().splitlines()
        test = data[7]
        f.close()
    except:
        data = ['','','','','','','','']
    layout = [[sg.Button("MANAGE DATABASE", key="manageDB")]
    ,[sg.Text("Database configuration", size=(20,0), font=('bold'))]
    ,[sg.Text('Host', size =(20, 0), font=('bold')), sg.InputText(data[0])]
    ,[sg.Text('User', size =(20, 0), font=('bold')), sg.InputText(data[1])]
    ,[sg.Text('Password', size =(20, 0), font=('bold')), sg.InputText(data[2])]
    ,[sg.Text('Database', size =(20, 0), font=('bold')), sg.InputText(data[3])]
    ,[sg.Text("Twitter API configuration", size=(20, 0), font=('bold'))]
    ,[sg.Text('API Key', size =(20, 0), font=('bold')), sg.InputText(data[4])]
    ,[sg.Text('API secret Key', size =(20, 0), font=('bold')), sg.InputText(data[5])]
    ,[sg.Text('Access Token', size =(20, 0), font=('bold')), sg.InputText(data[6])]
    ,[sg.Text('Access secret Token', size =(20, 0), font=('bold')), sg.InputText(data[7])]
    ,[sg.Button("SAVE", size=(20, 0), key="saveB"), sg.Button("EXIT", size=(20, 0), key="exitB")]
    ]
    window = sg.Window("Settings", layout, modal=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "exitB"):
            window.close()
            break
        elif event == "saveB":
            print("Settings saved.")
            configFile(values)
            window.close()
            break
        elif event == 'manageDB':
            createDatabaseWindow(data[0], data[1], data[2], data[3])


def startWindow():
    layout = [
      [sg.Text("Big BOT Chester")]
    , [sg.Button("START", size=(20, 0), key = "start"), sg.Button("STOP", size=(20, 0), key = "stop", disabled=True), sg.Button("SETTINGS", size=(20, 0), key = "config"), sg.Button("EXIT", size=(20, 0), key = "exit")]
    , [sg.Output(size = (100, 20), key = "-OUTPUT-")]]

    window = sg.Window("Big BOT Chester", layout, element_justification = 'c')
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "exit"):
            break
        elif event == 'start':
            window['start'].update(disabled=True)
            window['exit'].update(disabled=True)
            window['config'].update(disabled=True)
            window['stop'].update(disabled=False)
            window.FindElement('-OUTPUT-').Update('')
            print('Log cleared...\n')
            print('Initializing BOT...\n')
            t = threading.Thread(target=main)
            t.start()
        elif event == 'stop':
            window['start'].update(disabled=False)
            window['stop'].update(disabled=True)
            window['exit'].update(disabled=False)
            window['config'].update(disabled=False)
            print('\nBOT kill requested, waiting for last execution to finish...')
            t.do_run = False
        elif event == 'config':
            configWindow()

    window.close()



startWindow()
