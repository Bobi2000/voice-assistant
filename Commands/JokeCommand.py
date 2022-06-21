import requests

from Commands.Command import Command
from IO.output import speak


class JokeCommand(Command):
    def __init__(self, input): pass

    def execute(self):
        url = 'https://api.jokes.one/jod?category=knock-knock'
        headers = {'content-type': 'application/json'}

        response = requests.get(url, headers=headers)
        jokes = response.json()['contents']['jokes'][0]
        joke = jokes['joke']['text']
        print(joke)
        speak(joke)
