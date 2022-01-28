import pymorphy2
import pymystem3
m1 = pymorphy2.MorphAnalyzer()
m2 = pymystem3.Mystem()

#print(m1.parse(' 0030000838 Наконечники до 20 мкл (от 0,1 мкл), Standard, 40 мм, 2х500 шт/уп, Eppendorf'))
#print(m1.parse(' 0030000854 Наконечники до 20 мкл (от 0,5 мкл), 46 мм, 2х500 шт/уп, Eppendorf'))
if m1.parse(' 0030000838 Наконечники до 20 мкл (от 0,1 мкл), Standard, 40 мм, 2х500 шт/уп, Eppendorf') == m1.parse(' 0030000854 Наконечники до 20 мкл (от 0,5 мкл), 46 мм, 2х500 шт/уп, Eppendorf'):
    print('gg')