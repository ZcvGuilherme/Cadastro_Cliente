import pyautogui
import time

print("5 segundos")
time.sleep(5)

x, y = pyautogui.position()                             

print(f"X: {x}, Y: {y}")