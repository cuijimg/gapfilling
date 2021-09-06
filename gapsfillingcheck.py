# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:45:33 2021

@author: F-CUI
"""

# Filling the gaps
import pandas as pd
from fuzzywuzzy import fuzz
from pathlib import Path

file = Path( r"E:\policies_output\00\2010300452-18.csv" )


df = pd.read_csv(file, index_col=0, encoding="utf-8")
df['filled']=df['content']

print(df)
for i in range(len(df)-2):
    if str(df.loc[i,'filled']) != 'nan':
        for j in range(i+2,len(df)):
            if str(df.loc[j,'filled']) != 'nan':
                Ratio = fuzz.ratio(str(df.loc[i,'filled']),str(df.loc[j,'filled']))
                if Ratio >= 95:
                    for k in range(i+1,j):
                        df.loc[k,'filled'] = df.loc[j,'filled']
                else:
                    break
print(df)
print(111)
aaa = fuzz.ratio(str(df.loc[23,'filled']),str(df.loc[20,'filled']))
print(aaa)
# df.to_csv(file, encoding="utf-8")
                