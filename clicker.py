import sys
import time
import threading

from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

active = False
mouse = Controller()

def click ():
    while True:
        if active == True:
            mouse.click(Button.left)
            time.sleep(1 /15)

thread = threading.Thread(target=click, args=(), daemon=True)
thread.start()

def on_press (key):
    if hasattr(key, 'char'):
        if key.char == 'v':
            move_mouse()
            toggle()
    else:
        if key == Key.esc:
            sys.exit()

def move_mouse ():
    mouse.position = (300, 500)

def toggle ():
    global active
    active = not active

with Listener (on_press=on_press) as listener:
    listener.join()
