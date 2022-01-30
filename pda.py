import pandas as pd
loaded_data = pd.read_csv('really_withoutarc.csv', sep='\t', )
print(loaded_data.head(50000
                       ))
print( loaded_data['Номенклатура'][25365])