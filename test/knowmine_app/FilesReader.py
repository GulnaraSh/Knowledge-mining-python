# -*- coding: utf-8 -*-
"""
Function accessing the files in a user provided folder
and returning the list of file names

"""


import os


def get_file_names(folder):
    pdfFileNames = []
    
    # Get pdf fileName in folder
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.pdf') ): 
            pdfFileNames.append(folder+filename)
    return pdfFileNames

