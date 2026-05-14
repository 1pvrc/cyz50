from questionary import select
from src.pacc.config import MAIN_MENU

def mainMenu():
    selection = select(
        "Choose an option",
        choices=MAIN_MENU
    ).ask()
    return selection