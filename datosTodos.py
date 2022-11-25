import os
import pandas as pd

path = os.getcwd()
files = os.listdir(path)
files

files_xls = [f for f in files if (f[-5:] == '.xlsx') & (f!='resultadosTodos.xlsx')]

df = pd.DataFrame()

for f in files_xls:
    
    data = pd.read_excel(f, sheet_name='Sheet1')
    df = pd.concat([df,data])
    


file_name = 'resultadosTodos.xlsx'
df.to_excel(file_name, sheet_name='resume')

