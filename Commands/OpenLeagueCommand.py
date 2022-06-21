import os
import subprocess

from Commands.Command import Command
from IO.output import speak


class OpenLeagueCommand(Command):
    def __init__(self, input): pass

    def execute(self):
        os.startfile ("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\League of Legends.lnk")



