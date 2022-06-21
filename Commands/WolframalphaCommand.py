import wolframalpha

from Commands.Command import Command
from IO.output import speak

class WolframalphaCommand(Command):
    def __init__(self, input): 
        self.input = input

    def execute(self):
        app_id = 'GAQE36-QQQ6QXY4PY'
        client = wolframalpha.Client(app_id)
        res = client.query(self.input)
        answer = next(res.results).text
        print(answer)
        speak(answer)

