#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Author : Oguz Pamuk
Date   : 12.11.2016
'''

import hashlib
import os.path

filePath = "path"

### String olarak verilen inputun md5 olarak hash degerini dondurur
def getMD5ValueForString(plaintext):
	instance = hashlib.md5()
	instance.update(plaintext)
	return instance.hexdigest()

print getMD5ValueForString("oguz")

## Dosyanin icerigine gore md5 hash degerini dondurur
def getMD5ValueForFile(filepath):

	if not os.path.exists(filepath):
		print "file not found!"
	else:
		with open(filepath) as fileP:
			data = fileP.read()
			return hashlib.md5(data).hexdigest()

print getMD5ValueForFile(filePath)

def compareHashValues(input1,input2):
	if input1 == input2:
		return true
	else:
		return false




