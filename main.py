from Commands.GreetCommand import GreetCommand
from Commands.ShutdownCommand import ShutdownCommand
from IO.output import speak
from IO.input import takeCommand

commands = {"greet": GreetCommand, "goodbye bye stop": ShutdownCommand}

def interpetCommand(statement):
        result = [x.strip() for x in statement.split(' ')]

        for key in commands:
            argsKey = key.split(' ')

            counter = 0

            for a in argsKey:
                for b in result:
                    if a == b: pass


        print(result)
        #speak('Good bye')

if __name__ == '__main__':


    commands["greet"].execute()

    while True:
        statement = takeCommand().lower()

        if statement == 0:
            continue

        interpetCommand(statement)
