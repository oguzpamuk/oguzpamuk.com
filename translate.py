#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author : Oguz Pamuk

Daha detaylı bilgi icin http://pythonhosted.org/goslate/ ziyaret edebilirsiniz.
'''

import goslate

gs = goslate.Goslate()

languages = gs.get_languages()

print "Desteklenen Diller ve Kullanımı"

for keys,values in languages.items():
    print(keys + " : " + values)

try:
	print(gs.translate('o okula gitti', 'en'))
except Exception:
	print "Service Unavailable"


