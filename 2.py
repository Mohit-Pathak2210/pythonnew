import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv("m.csv", index_col = "Name")


#print(df.loc["Charizard": "Pikachu",["Type1","Type2","Legendary"]])
pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")
