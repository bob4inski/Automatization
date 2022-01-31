import pymorphy2
import pymystem3
m1 = pymorphy2.MorphAnalyzer()
m2 = pymystem3.Mystem()

c = m1.parse('обьяна')[0]
print(c.normal_form)

from ctypes import cdll
from ntpath import join
import pandas as pd
import string
import textdistance
loaded_data = pd.read_csv('tests_2.csv', sep='\t', )
print(loaded_data.head(100))