
import pyautogui as pag
import random as r
import time
z=0
while z==0:
    x = r.randint(600,700)
    y = r.randint(200,600)

    pag.moveTo(x,y,0.5)
    time.sleep(2)
