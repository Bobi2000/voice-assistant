import webbrowser

from Commands.Command import Command
from IO.output import speak

class OpenBrowserCommand(Command):
    def __init__(self, input): 
        self.input = input
        print(input)

    def execute(self):
        if 'youtube' in self.input:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'google' in self.input:
            speak("Opening google")
            webbrowser.open("google.bg")
        
        elif 'overflow' in self.input:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")
