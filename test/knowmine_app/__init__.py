"""
The knowmine module
======================
The " knowmine app"extracts potentially relevant sentences from the collection of scientific articles.
Currently a User should provide a path to the collection of texts in pdf format and list of keywords for 
the extraction.

"""
import knowmine_app.files
import knowmine_app.texts
import os 
import sqlite3
from sqlite3 import Error
import json 
import time
import concurrent.futures

#User defined path to the collection of articles
folder_path = 'X:\\Gulnaras mapp\Textmining\WOS\\Aquatic toxicity\\'

#User defined keywords
words = ["increas", "decreas", "relationship", "correlat", "structur", "fragment", "class", "compound", "molecul", "significant", "high", "affect"]
keys =["toxicit","acute", "LC50", "EC50"] 



#for many articles
def get_relevant_sentences(folder_path):
    start_time = time.time()
    print("--- %s seconds ---" % (start_time))
    path = folder_path
    database = r"C:\Test\TestDatabase.db"
    
    processedFile =	{
      "filename": filename
    }
    
    
    folder = os.fsencode(path)
    pdfFileNames = files.get_file_names(folder)
    
    
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
            res = executor.map(texts.processFile, pdfFileNames)
            
            for result in res:
                conn = create_connection(database)
                with conn:
                    add_result_to_database(conn, result)
                            
    
    print("--- %s seconds ---" % (time.time() - start_time))
    
