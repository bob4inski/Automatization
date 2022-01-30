import pymorphy2
import pymystem3
m1 = pymorphy2.MorphAnalyzer()
m2 = pymystem3.Mystem()

print(m1.parse('обезьяна'))

print(m1.parse)