#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Author : Oguz Pamuk
Date   : 12.11.2016
'''

import hashlib


def getSHA1ValueForString(plaintext):
	instance = hashlib.sha1()
	instance.update(plaintext)
	return instance.hexdigest()


def getSHA224ValueForString(plaintext):
	instance = hashlib.sha224()
	instance.update(plaintext)
	return instance.hexdigest()

def getSHA256ValueForString(plaintext):
	instance = hashlib.sha256()
	instance.update(plaintext)
	return instance.hexdigest()

def getSHA384ValueForString(plaintext):
	instance = hashlib.sha384()
	instance.update(plaintext)
	return instance.hexdigest()

def getSHA512ValueForString(plaintext):
	instance = hashlib.sha512()
	instance.update(plaintext)
	return instance.hexdigest()


print getSHA1ValueForString("oguz")
print getSHA224ValueForString("oguz")
print getSHA256ValueForString("oguz")
print getSHA384ValueForString("oguz")
print getSHA512ValueForString("oguz")


