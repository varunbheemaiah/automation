import pyautogui

pyautogui.FAILSAFE = True
pyautogui.moveTo(270,1050,duration=2)
pyautogui.click(270,1050)
pyautogui.typewrite("Paint",0.5)
pyautogui.typewrite(['enter'])
inx,iny=569,313
pyautogui.moveTo(inx,iny,duration=1)
d=200
while d>0:
    pyautogui.dragRel(d,0,duration=2)
    d=d-10
    pyautogui.dragRel(0,d,duration=2)
    pyautogui.dragRel(-d,0,duration=2)
    d=d-10
    pyautogui.dragRel(0,-d,duration=2)
