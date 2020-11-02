"""
The knowmine module
======================

Gets the folder path containing the relevant articles for knowledge mining and returns potentially relevant sentences 
as SQL database

"""
import knowmine_app.files
import knowmine_app.texts
import os 
import sqlite3
from sqlite3 import Error
import json 
import time
import concurrent.futures


folder_path = 'X:\\Gulnaras mapp\Textmining\WOS\\Aquatic toxicity\\'


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def add_result_to_database(conn, result):
    sql = ''' INSERT INTO ANALYSED_SENTENCES(Path, CleanedSentences, KeyWordsOfSentences, UsefulSentences)
              VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, result)
    conn.commit()     

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
    
