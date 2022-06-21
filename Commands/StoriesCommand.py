import requests

from Commands.Command import Command
from IO.output import speak

class StoriesCommand(Command):
    def __init__(self, input): pass

    def execute(self):
        url = 'https://shortstories-api.herokuapp.com/'
        headers = {'content-type': 'application/json'}

        response = requests.get(url, headers=headers)
        story = response.json()
        #story = response.json()['content']

        authorText = story['title'] + " by " + story['author']
        moral = 'the moral of the story is that: ' + story['moral']

        print(authorText)
        speak(authorText)

        print(story['story'])
        speak(story['story'])

        print(moral)
        speak(moral)
