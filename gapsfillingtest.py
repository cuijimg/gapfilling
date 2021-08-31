import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz

np.random.seed(0)

df = pd.DataFrame(np.random.randint(1,20,size=(20,4)),columns=list('abcd'))
df['content']=''
df.loc[3,'content']='wer will das essen? ich will ich will ich will!'
df.loc[6,'content']='wer will das essen? ich will ich will ich will'

df.loc[10,'content']='wer will?'
df.loc[13,'content']='wer wills'
df.loc[18,'content']='wer wills'
df.loc[19,'content']='wer wills'
print(df)
for i in range(len(df)-2):
    for j in range(i+2,len(df)):
        if (str(df.loc[i,'content']) != '') & (str(df.loc[j,'content']) != ''):
            Ratio = fuzz.ratio(str(df.loc[i,'content']),str(df.loc[j,'content']))
            if Ratio >= 95:
                for k in range(i+1,j):
                    df.loc[k,'content'] = df.loc[j,'content']
print(df)            
df.to_csv(r'C:\Users\F-CUI\Desktop\ZEW\gapfilling\result.csv', encoding="utf-8")