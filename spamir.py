import pyautogui as auto
import time 

time.sleep(4)
while True:
    auto.write('whats up?')
    auto.press('enter')
    time.sleep(0.001)
