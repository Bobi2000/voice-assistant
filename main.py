import threading
import tkinter
import customtkinter
import keyboard

from Commands.GreetCommand import GreetCommand
from Commands.JokeCommand import JokeCommand
from Commands.OpenBrowserCommand import OpenBrowserCommand
from Commands.OpenLeagueCommand import OpenLeagueCommand
from Commands.ShutdownCommand import ShutdownCommand
from Commands.StoriesCommand import StoriesCommand
from Commands.WikipediaCommand import WikipediaCommand
from Commands.WindowsCommand import WindowsCommand
from Commands.WolframalphaCommand import WolframalphaCommand
from IO.input import takeCommand
from IO.output import speak

commands = {
    "greet": GreetCommand,
    "goodbye bye stop": ShutdownCommand,
    "wikipedia wiki pedia": WikipediaCommand,
    "lol league of legends": OpenLeagueCommand,
    "open": OpenBrowserCommand,
    "tell me joke": JokeCommand,
    "tell me stories story short text": StoriesCommand,
    "wolfram alpha wolf ram": WolframalphaCommand,
    "windows window windows10": WindowsCommand
}

def interpetCommand(statement):
    result = [x.strip() for x in statement.split(' ')]

    actionCount = -100
    actionKey = ""
    action = None

    for key in commands:
        argsKey = key.split(' ')

        counter = 0
        curAction = commands[key]

        for a in argsKey:
            for b in result:
                if a == b:
                    counter += 1

            if actionCount < counter:
                actionCount = counter
                action = curAction
                actionKey = key

    if actionCount <= 0:
        return

    args = statement
    curArgs = [x.strip() for x in actionKey.split(' ')]

    for arg in curArgs:
        args = args.replace(arg, '')

    action(args).execute()


def main():
    # interpetCommand("league of legends lol")

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    app.title("Voice Assistant")
    app.geometry("800x500")

    frameCnt = 24
    frames = [tkinter.PhotoImage(
        file='Assets/assistant.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        app.after(70, update, ind)

    label = tkinter.Label(app)
    label.pack()
    app.after(0, update, 0)
    app.mainloop()


def assistantMain():

    interpetCommand("greet")

    while True:
        try:
            if keyboard.is_pressed('`'):
                statement = takeCommand().lower()
                if statement == 0:
                    continue

                interpetCommand(statement)
        except:
            print('No such command')


if __name__ == '__main__':

    assistantThread = threading.Thread(target=assistantMain)
    assistantThread.daemon = True
    assistantThread.start()

    main()


