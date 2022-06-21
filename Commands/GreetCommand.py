import datetime
from Commands.Command import Command
from IO.output import speak


class GreetCommand(Command):
    def __init__(self, input): pass

    def execute(self):
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            speak("Hello, Good Morning")
            print("Hello, Good Morning")
        elif hour >= 12 and hour < 18:
            speak("Hello, Good Afternoon")
            print("Hello, Good Afternoon")
        else:
            speak("Hello, Good Evening")
            print("Hello, Good Evening")
