from Commands.Command import Command
from IO.output import speak


class ShutdownCommand(Command):
    def __init__(self, input): pass

    def execute(self):
        speak('your personal assistant is shutting down, Good bye')
