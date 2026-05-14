import pandas as pd
import os
from src.pacc.config import FILE_NAME

def create():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=[
            "Date",
            "Note",
            "Type",
            "Debit",
            "Credit"
        ])
        df.to_csv(FILE_NAME, index=False)


def load_data():
    return pd.read_csv(FILE_NAME)

def save_data(df):
    df.to_csv(FILE_NAME, index=False)




def inc(a, b, c, d):
    new_data = {
        "Date": a,
        "Note": b,
        "Type": c,
        "Debit": d
        
    }

    df = load_data()

    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    save_data(df)

    print("\n Transaction added!\n ")


def exp(a, b, c, d):
    new_data = {
        "Date": a,
        "Note": b,
        "Type": c,
        "Credit": d
        
    }

    df = load_data()

    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    save_data(df)

    print("\n Transaction added!\n ")





def show_balance():
    df = load_data()

    if df.empty:
        print("Current Balance: 0")
        return

    income = df["Debit"].sum()
    expense = df["Credit"].sum()

    balance = income - expense

    print(f"\n Current Balance: {balance}\n ")