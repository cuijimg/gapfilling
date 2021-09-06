# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:45:33 2021

@author: F-CUI
"""

# Filling the gaps
import pandas as pd
from fuzzywuzzy import fuzz
from pathlib import Path

path = Path( r"E:\policies_output" )
folders= [format(i, '#04x')[2:4] for i in range(256)] # generating a list of the folder names in the format of #04x
folders_given = [g.name for g in path.glob('*')]
if all([f in folders_given for f in folders]): # check if the folders are correct
    for folder in folders:
    # for folder in folders[12:]: #change it back later!!!
        
        path = Path( r"E:\policies_output" ) / folder
        files = list(path.glob("*.csv"))
        print(folder, path)
        # print(files)
        
        for file in files: 
            print(folder, file)
            df = pd.read_csv(file, index_col=0, encoding="utf-8")
            df['filled']=df['content']
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
            
            df.to_csv(file, encoding="utf-8")
                