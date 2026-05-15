import questionary

MAIN_MENU = ["Add Income", "Add Expenses", "View Balance", "Exit"]


accounts = ['data/work.csv', 'data/private.csv']
FILE_NAME = questionary.select(
    "Select an account: ",
    choices = accounts
).ask()


