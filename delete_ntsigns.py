#coding=utf-8
"""
Created on Mon Jul  5 12:25:16 2021

@author: Jimmy Cui
"""
# delete \n, \t, urls for the texts, for readability test later

import csv
import pandas as pd
import re



from pathlib import Path
path = Path( r"E:\policies_output" )
folders= [format(i, '#04x')[2:4] for i in range(256)] # generating a list of the folder names in the format of #04x
folders_given = [g.name for g in path.glob('*')]
if all([f in folders_given for f in folders]): # check if the folders are correct
    for folder in folders:
        
        path = Path( r"E:\policies_output" ) / folder
        files = list(path.glob("*.csv"))
        print(folder, path)
        # print(files)
        
        for file in files: 
            print(folder, file)
            df = pd.read_csv(file, index_col=0, encoding="utf-8")
            for index, row in df.iterrows():
                csvinfo = row['content']
                
                if csvinfo != 'nan':
                    csvinfo = re.sub(r'[\n|\t]','',csvinfo)
                    csvinfo = re.sub(r"(https?|ftp|file):\/\/[-A-Za-z0-9+&@#\/%?=~_|!:,.;]+[-A-Za-z0-9+&@#\/%=~_|]",'',csvinfo)

            # print(df['content'])
            df.to_csv(file, encoding="utf-8")
            
            # # for further check
            # df = pd.read_csv(file,usecols=['content'], encoding="utf-8") 
            # print(df['content'])
            # break
   


