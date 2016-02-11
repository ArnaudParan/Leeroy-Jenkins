# -*- coding: utf-8 -*-

"""
Fonctions.py
"""

# Utilities
import os, sys
# Maths with Numpy
import numpy as np


####### Some Tools ####################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################

bcolors = {
    'red' : '\033[91m',
    'green' : '\033[92m',
    'blue' : '\033[94m',
    'cyan' : '\033[96m',
    'white' : '\033[97m',
    'yellow' : '\033[93m',
    'magenta' : '\033[95m',
    'grey' : '\033[90m',
    'black' : '\033[90m',
    'default' : '\033[99m',
    'endc' : '\033[0m',
    'bold' : '\033[1m',
    'underline' : '\033[4m',
    }


def color_print(color, s, bold=True):
    to_print = ""
    if bold:
        to_print = bcolors['bold']
    to_print = to_print + bcolors[color] + s + bcolors['endc']
    print to_print

def debug_print(s):
    color_print('red', s)



####### Data loading and writting functions ###################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################


def read_input(_file):
    if not '.in' in _file:
        color_print("red", "Fatal : dataset must be a .in file ! Quitting" )
        exit()
    # reads the dataset
    try:
        with open(_file, 'rb') as infile:
            # read all lines
            data = [line.rstrip('\n') for line in infile]
            # first line is special
            args = data[0].split()
            data = data[1:]
        return int(args[0]), int(args[1]), data
    except:
        color_print("red", "Error : cannot read data file : " + _file)
        exit()




