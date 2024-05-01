import pandas as pd

def convert():
    with open('data.json', encoding='utf-8') as inputfile:
        df = pd.read_json(inputfile)
    df.to_csv('data.csv', encoding='utf-8', index=False)