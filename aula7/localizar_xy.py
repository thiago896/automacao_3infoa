#importa a biblioteca que controla o mouse e o teclado
import pyautogui

#localiza as coordenadas de um elemento na tela 
#usando uma imagem
xy = pyautogui.locateCenterOnScreen("aula7\\8.png", confidence=0.99)
pyautogui.click(xy,duration=1)

xy = pyautogui.locateCenterOnScreen("aula7\\x.png", confidence=0.80)
pyautogui.click(xy,duration=1)

xy = pyautogui.locateCenterOnScreen("aula7\\3.png", confidence=0.99)
pyautogui.click(xy,duration=1)

xy = pyautogui.locateCenterOnScreen("aula7\\igual.png", confidence=0.99)
pyautogui.click(xy,duration=1)