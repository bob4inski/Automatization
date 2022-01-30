from ctypes import cdll
from ntpath import join
import pandas as pd
import string
import textdistance
import pymorphy2
import pymystem3
m1 = pymorphy2.MorphAnalyzer()
m2 = pymystem3.Mystem()

def delete_arc(data):
    data = data.lower()
    mass = data.split()
    arr = ['1', '4', '5', '6', '7', '8', '9', '0']
    for i in arr:
        if i in mass[0]:
            del mass[0]
            mass = ' '.join(mass)

            return mass
    else:
        mass = ' '.join(mass)
        return mass

def key(data):
    data_set = data.split( )
    chers = string.ascii_lowercase
    len_data_set = len(data_set)
    for lenght in  range(len_data_set):
        for chars in chers:
            try:
                if chars in data_set[lenght]:
                    del data_set[lenght]
                    break
            except:
                data = ' '.join(data_set)
                return data

    data = ' '.join(data_set)
    return data


def numbers_and_trash(data):
    numbers = string.digits
    trash = [',','(','/','|','-']
    data_set = data.split()
    tram = []
    without_num = []
    k = 0
    len_data_set = len(data_set)
    for datas in range(1,len_data_set):
        for i in numbers:
            if i in data_set[datas]:
                k += 1
        if k ==0:
            without_num.append(data_set[datas])
        else:
            tram.append(data_set[datas])
    tram = ' '.join(tram)
    without_num =' '.join(data_set)
    return without_num

def minus_dwa_or_tri(data):
    data_set = data.split()
    #len_data_set = len(data_set)
    result = []
    try:
        result.append(data_set[0])
        result.append(data_set[1])
        result.append(data_set[2])
        result = ' '.join(result)
        return result
    except:
        try:
            result.append(data_set[0])
            result.append(data_set[1])
            result = ' '.join(result)
            return result
        except:
            try:
                result.append(data_set[0])
                result = ' '.join(result)
                return result
            except:
                return 'Sorry, my bad'

loaded_data = pd.read_csv('Задание.csv', sep='\t', )
#print(loaded_data.head(100))
loaded_data.insert(1, 'first', 'second', 'third')

len_dataframe = len(loaded_data)
loaded_data[['first', 'second', 'third']] = None

for i in range(len_dataframe):
    loaded_data['Номенклатура'][i] = delete_arc(loaded_data['Номенклатура'][i])
    #loaded_data['first'][i] = key(loaded_data['Номенклатура'][i])
    loaded_data['first'][i] = m1.parse(minus_dwa_or_tri(key(loaded_data['Номенклатура'][i])))
    loaded_data['second'][i] = m1.parse(loaded_data['first'][i])


loaded_data.sort_values(by='Номенклатура')

print(numbers_and_trash( key(delete_arc(loaded_data['Номенклатура'][260]))))
loaded_data.to_csv('really_withoutarc.csv', index=False)

print(loaded_data.head(100))




