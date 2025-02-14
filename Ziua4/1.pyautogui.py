import pyautogui
import random
import time

dimensiuni = pyautogui.size()
print(dimensiuni, type(dimensiuni))

height = dimensiuni.height 
width =  dimensiuni.width

print(height, width)

start_time = time.time()
duration =  20 # secunde
while time.time() - start_time < duration:
    random_height = random.randint(0, height)
    random_width = random.randint(0, width)
    print(f"Se va muta la ({random_width}, {random_height})")
    pyautogui.moveTo(random_width, random_height, duration=1)
    time.sleep(3)