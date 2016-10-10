#!/usr/bin/python
import random

'''
Author    : Oguzcan Pamuk
Reference : https://docs.python.org/2/library/random.html
'''


# random olarak bir integer sayi elde etmek icin (1 <= x <= 10)
print random.randint(1, 10)  

# random float sayi olusturma (0.0 <= x < 1.0)
print random.random()

# araligi kendimiz belirleyerek random sayi olusturmak icin (1.0 <= x  <3.0)
print random.uniform(1, 3)

# elimizde bir string var,bu listeden random olarak bir elemani secebilmek icin
print random.choice('12345678')

# elimizdeki listenin elemanlarinin random olarak yer degistirebilmesi icin
liste = [1,2,3,4,5,6,7]
random.shuffle(liste)
print liste
# elimizdeki liste icerisinden random olarak istedigimiz eleman sayisina sahip bir liste olusturabilmek icin

liste = ['a','b','c','d','e','f']
#2 elemanli yeni bir liste olusturacak
print random.sample(liste,2)



