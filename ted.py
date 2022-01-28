from ctypes import cdll
import pandas as pd

import textdistance



loaded_data = pd.read_csv('Задание.csv', sep='\t',)
print(loaded_data.head(100))
loaded_data.insert(1,'first','second','third')

len_dataframe = len(loaded_data)

'''
#loaded_data[['first','second','third']] = None

for i in range(len_dataframe -1 ):
    for g in range(i+1,len_dataframe):
        if textdistance.hamming.normalized_distance(loaded_data[i][0], loaded_data[g][0]) < 0.3:
            if loaded_data[i][first] == None and loaded_data[g][first]== None:
                loaded_data[g][first] = loaded_data[i][0]
                
            

print(loaded_data.head(100))
print(len_dataframe)'''