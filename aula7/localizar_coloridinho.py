import pyautogui

for i in range(100):
    xy = pyautogui.locateCenterOnScreen(
    "aula7\\bola.png",
    confidence=0.80,
    grayscale=False
    )
    pyautogui.click(xy)
    i = 1 + i
    