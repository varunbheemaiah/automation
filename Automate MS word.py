import pyautogui
import time

time.sleep(3)

pyautogui.press('win',interval=0.3)
time.sleep(2)
pyautogui.write('word',interval=1)
pyautogui.press('enter',interval=2)
time.sleep(2)

pyautogui.hotkey('ctrl','n',interval=1)

pyautogui.press('Enter',interval=0.25)
pyautogui.press('Enter',interval=0.25)



time.sleep(2)

pyautogui.write(" Write Your Message :)")

time.sleep(2)
pyautogui.hotkey('ctrl','s',interval = 1)
pyautogui.press('Enter')

time.sleep(2)






