import keyboard
import time
from rich import print
from rich.console import Console
from rich.text import Text
from rich.style import Style

banner = f"""
[bold][red]
                               _         _   
        ____ __  __ _ _ __ ___| |__  ___| |_ 
       (_-< '_ \/ _` | '  \___| '_ \/ _ \  _|
       /__/ .__/\__,_|_|_|_|  |_.__/\___/\__|
          |_|                  [/bold][/red]              
                                                [bold][blue]Github: nightx64[/blue][/bold]               [bold magenta ]Twitter: nightx64[/bold magenta ]                                              
                                                [dark_green]Instagram: nightsecurity2023[/dark_green]
"""


def options():
  message = input("Message to spam: ")
  duration = input("Message sending time(has to be less than 1): ")
  repeats = input("how many messages do you want to send: ")

  time.sleep(10)

  for i in range(int(repeats)):
    keyboard.write(message)
    keyboard.press_and_release("enter")
    time.sleep(float(duration))


def menuzinho():
  print(
    "              [cyan]|[/cyan] [1] Start      [2] Exit [cyan]|[/cyan]\n")

  while True:
    escolha = input("==> ")

    if escolha == "1":
      time.sleep(1)
      print("initializing.. ")
      options()
    if escolha == "2":
      break


def main():
  print(banner)
  menuzinho()


main()
