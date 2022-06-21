import wikipedia

from Commands.Command import Command
from IO.output import speak


class WikipediaCommand(Command):
    def __init__(self, input): 
        self.input = input

    def execute(self):
        print(self.input)
        # speak('Searching Wikipedia...')
        results = wikipedia.summary("New England Patriots", sentences=5) 
        speak("According to Wikipedia")
        print(results)
        speak(results)
