# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:47:16 2020

@author: gulsha
"""


import sqlite3
from sqlite3 import Error
import concurrent.futures

import os

class SQLoutput:
    
     def __init__(self, db_name, output):
        self.dbname = db_name
        self.output = output
        
        
     def create_connection(self):
         """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
         conn = None
         try:
             conn = sqlite3.connect('{self.dbname}.db')
         except Error as e:
             print(e)
    
         return conn
    
     def add_result_to_database(conn, result):
         sql = ''' INSERT INTO ANALYSED_SENTENCES(Path, CleanedSentences, KeyWordsOfSentences, UsefulSentences)
                  VALUES(?,?,?,?)'''
         cur = conn.cursor()
         cur.execute(sql, result)
         conn.commit()    

