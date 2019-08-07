import pyautogui
from time import sleep
sleep(5)
for i in range(200):
    pyautogui.moveTo(596,632)
    sleep(0.25)
    pyautogui.click(596,632)
    sleep(0.25)
    pyautogui.moveTo(854,450)
    sleep(0.25)
    pyautogui.click(854,450)
    print(i)