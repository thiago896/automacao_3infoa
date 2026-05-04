import pyautogui
import time          

def pesquisarNoGPT():
    #abre um endereço
    pyautogui.write('http://www.chatgpt.com')
    pyautogui.press('enter')

    #faz uma pausa
    time.sleep(3)

    #faz uma pesquisa no chatgpt
    pyautogui.write(pesquisa)
    pyautogui.press('enter')

    #tenta clicar na imagem copia
    while True:
        time.sleep(2)
        try:
            xy = pyautogui.locateCenterOnScreen('aula8\\copiar.png', confidence=0.98)
            pyautogui.click(xy)
            break
        except:
            pyautogui.press('pagedown')


#criar função para enviar email
def enviarEmail():
    #atalho para abrir nova guia
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.write('www.gmail.com')
    pyautogui.press("enter")
    time.sleep(3)
    escrever = pyautogui.locateCenterOnScreen('aula8\\escrever.png', confidence=0.95)
    pyautogui.click(escrever)

    pyautogui.write('Lucas Costa <lucas5.costa@alunos.ifsuldeminas.edu.br>', inteval=0.1)
    pyautogui.press('tab')
    pyautogui.write("oi menino", interval=0.1)
    pyautogui.press('tab')
    pyautogui.write("vamos almoçar meio dia ", interval=0.1)

    enviar = pyautogui.locateCenterOnScreen('aula8\\enviar.png', confidence=0.95)
    pyautogui.click(enviar)







#Parte Principal do Programa

#abre uma janela para o usuário digitar um texto
pesquisa = pyautogui.prompt('O que você quer pesquisar hoje?')
abrirChrome()
enviarEmail()
