# Transaction Recording CLI Tool

A lightweight, interactive command-line tool for tracking personal finances. Built with `pandas` to record income, expenses, and maintain a complete transaction history with real-time balance updates. All data persists locally in CSV format for easy analysis in Excel, Google Sheets, or any data analysis tool.


> **Learning Note:** This project was created to practice `pandas` data manipulation, but it's fully functional for daily financial tracking!

Clone the repo using:
```Bash
git clone https://github.com/1pvrc/transaction-recorder.git
mkdir transaction-recorder
```

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