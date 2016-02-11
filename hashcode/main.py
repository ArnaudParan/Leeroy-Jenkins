# -*- coding: utf-8 -*-

"""
HASHCODE Main
"""

# Utilities
import os, sys, copy
# Maths with Numpy
import numpy as np
# Options parmeters
from optparse import OptionParser
# tools
from fonctions import *
# code
from peinture import *


####### Main of script ################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################


if __name__ == '__main__':

    # Programm parameters
    # ==========================================================================================

    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input", default="", help="Path to input file")
    parser.add_option("-o", "--output_path", dest="output_path",default="./output.csv", help="Path to output")
    parser.add_option("-m", "--method", dest="method",default="1", help="method")
    parser.add_option("-n", "--niter", dest="iterations",default="1", help="n iterations")


    (options, args) = parser.parse_args()

    # create dictionnry of options :
    options = {  "input"            : options.input,
                 "output_path"        : options.output_path,
                 "method"        : options.method,
                 "iterations"        : int(options.iterations),
                }


    # verify options :
    if options["input"]=="":
        color_print("red", "Error : no input found !")
        parser.print_help()
        exit()


    # load input
    color_print("blue", "Loading data from " + options["input"]+" ..." )
    nr, nc, data = read_input(options["input"])

    # convert data
    data = format_numpy(nr,nc,data)
    
    # Process data with given method
    color_print("blue", "Processing data with method n° " + options["method"]+" ..." )

    if options["method"] == '1':
        data_save = copy.copy(data)
        output = process_data_method1(nr, nc, data)

        # # Saving results
        # color_print("blue", "Saving file to " + options["output_path"] + " ..." )
        # write_commands(output, options["output_path"])
        # color_print("green", "Saving done !")


    else :
        color_print("red", "Error : wrong method !")
        parser.print_help()
        exit()

    
