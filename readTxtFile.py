import json 
import os
import pandas as pd

path = r'C:\Users\FayaadAbrahams\Desktop\Projects\JSONtoCSV'
files = os.listdir(path)
files_txt = [i for i in files if i.endswith('.txt')]
file_path = files_txt[0]
print('File name is: '+ file_path)

import json
with open(file_path) as f:
    json_data = json.load(f)
    f.close()
    df = pd.read_json(file_path)
    df.to_csv('Converted JSON.csv', encoding='utf-8', index=False)
    
print('Completed Process!')
    
    
    