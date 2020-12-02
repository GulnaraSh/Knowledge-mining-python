# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:05:15 2020

@author: gulsha
"""


import os
import knowmine_app.FilesReader as FilesReader
import knowmine_app.RelevantSentencesExtractor as rse
import concurrent.futures
import knowmine_app.OutputfileGenerator as of


folder = 'C:\\Users\gulsha\Desktop\Articles extra for mining\\'

words = ["increas", "decreas", "relationship", "correlat", "structur", "fragment", "class", "compound", "molecul", "significant", "high", "affect"]
keys =["toxicit","acute", "LC50", "EC50"]

def test_get_sentences(file):
    return file.get_relevant_sentences()

def test_extract_relevant_sentences(folder_path, main_terms, relation_words, outputfile_format="db"):
    
    n = int(os.cpu_count()/2)
    pdfFileNames = FilesReader.get_file_names(folder_path)
    list_of_articles = [rse.RelevantSentences(item, main_terms, relation_words) for item in pdfFileNames]
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=n) as executor:
        res = executor.map(test_get_sentences, list_of_articles)
    
    assert len(pdfFileNames) > 0
    assert len(list_of_articles) > 0
    assert res != None
                             
    
    