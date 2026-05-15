from src.pacc.select import mainMenu
from src.pacc.config import *
from src.pacc.dataframe.actions import *
from datetime import datetime
import pandas as pd
import os

def transaction(choice):
    if choice == MAIN_MENU[0]:
        t_type = "Income"
    elif choice == MAIN_MENU[1]:
        t_type = "Expense"
    amount = int(input("Enter an amount: "))
    note = input("Enter a note: ")
    date = datetime.now().strftime("%d-%m-%Y %H:%M")
    return date, note, t_type, amount



def logic():

    while True:
        selection = mainMenu()
        if selection == MAIN_MENU[0]:
            a, b, c, d = transaction(selection)
            if c == "Income":
                add_transactions(a, b, c, d, selection)

        elif selection == MAIN_MENU[1]:
            a, b, c, d = transaction(selection)
            if c == "Expense":
                add_transactions(a, b, c, d, selection)
        
        elif selection == MAIN_MENU[2]:
            show_balance()
            
        


        elif selection == MAIN_MENU[3]:
            break
