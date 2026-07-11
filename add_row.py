import pandas as pd
import os
from data_source import load_data

file_path = 'data/sample_data.csv'
df=load_data()

# Adding new row in data
new_row_loc = {'Name':'person2','Age':25,'City':'city2'}
df.loc[len(df.index)] = new_row_loc

df.to_csv(file_path, index=False)

print(f"New row added to {file_path}")