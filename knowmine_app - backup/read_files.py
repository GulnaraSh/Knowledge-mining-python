# -*- coding: utf-8 -*-
"""
Function accessing the files in a user provided folder and returning the list of file names

"""


import os


def get_file_names(folder):
    pdfFileNames = []
    
    # Get pdf fileName in folder
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.pdf') ): 
            # Do it directly, not using multiple threads: Uncomment below row
            #result = processFile(path + filename)
            #conn = create_connection(database)
            #with conn:
            #    add_result_to_database(conn, result)            
            # REMOVE ABOVE ROWS WHEN NOT DEBUGGING
            pdfFileNames.append(folder+filename)
    return pdfFileNames




folder = 'C:\\Users\gulsha\Desktop\Articles extra for mining\\'


c= get_file_names(folder)