# -*- coding: utf-8 -*-

"""
Fonctions.py
"""


# Utilities
import os, sys
# Maths with Numpy
import numpy as np

# convertie en np 0 1
def format_numpy(nr, nc, data):
	res = np.zeros([nr,nc])
	for i in range(0,nr):
		for j in range(0,nc):
			if data[i][j] == '#':
				res[i][j] = 1
	return res


# retourne une liste de tuple (densite, size)
def calcul_densite(nr, nc, data):
	


def process_data_method1(nr, nc, data):
	for i in range(nc):
		print data[i,:]