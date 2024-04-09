import os
import sys
from politiker import Politiker


def rens_terminal():
    if sys.platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

print("-- Velkommen til Stortinget_fantasy --")

while True:
    rens_terminal()
    print(" -- Stortinget-fantasy --")
    print("1: Vis politikeroversikt")
    print("2: Avslutt")
    brukervalg = input("> ")
    if brukervalg == "2":
        print("avslutter..")
        break

print("Takk for nå")