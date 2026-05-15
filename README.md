# Transaction Recording CLI Tool

This is a transaction recorder tool built with `pandas` to track Income, Expenses, Balance and Transaction History. and All transactions are stored in a CSV file for easy access and analysis.

I made this project to learn and practice `pandas` but you can still use it for recording your transactions

## Requirements

Create a Venv:
```bash
uv venv
source .venv/scripts/activate
```

and install the requirements:
```bash
uv pip install -r requirements.txt
```
or just:
```bash
uv pip install pandas questionary
```

## Usage

make sure you have a `data` folder inside root, if you dont run:
```bash
mkdir data
```

Run the application using:
```bash
py main.py
```