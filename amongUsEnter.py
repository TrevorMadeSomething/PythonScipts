import pynput
import time
import threading

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key

start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')
delay = .3
button = Button.left


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.position = (1231, 1302)
                time.sleep(.1)
                mouse.click(Button.left, 1)
                time.sleep(.1)
                keyboard.press(Key.ctrl)
                time.sleep(.1)
                keyboard.press('v')
                time.sleep(.1)
                keyboard.press(Key.ENTER)
                mouse.position = (602, 593)
                time.sleep(.1)
                mouse.click(Button.left, 1)
                time.sleep(.1)
            time.sleep(.3)


mouse = Controller()
keyboard = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
