import ctypes
import winshell

from Commands.Command import Command
from IO.output import speak

class WindowsCommand(Command):
    def __init__(self, input):
        self.input = input

    def execute(self):
        if 'lock' in self.input:
            print("locking the device")
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'empty recycle bin' in self.input:
            print("Recycle Bin Recycled")
            speak("Recycle Bin Recycled")
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)

