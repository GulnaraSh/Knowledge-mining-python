# -*- coding: utf-8 -*-
"""
Function accessing the files in a user provided folder and returning the list of file names

"""


import os



def test_get_file_names():
    pdfFileNames = []
    folder = r'C:\\Users\gulsha\Desktop\Articles extra for mining\\'
    # Get pdf fileName in folder
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.pdf') ): 
            pdfFileNames.append(folder+filename)
    assert len(pdfFileNames) > 0

