import pyautogui 
import time


def clickingButtons(image):
    button = pyautogui.locateCenterOnScreen(image, grayscale= True, confidence= .5)
    pyautogui.moveTo(button)
    pyautogui.click()

time.sleep(2)
#location
clickingButtons("from.png")
pyautogui.press('down')
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl","a")

pyautogui.write("09/02/2022")
# pyautogui.press("enter")
clickingButtons("general.png")
time.sleep(1)
clickingButtons("tatkal.png")


