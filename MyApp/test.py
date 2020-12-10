# -*- coding: utf-8 -*-
"""
Test for the knowmine main module
"""


import os
import knowmine_app.FilesReader as FilesReader
import knowmine_app.RelevantSentencesExtractor as rse
import concurrent.futures


def test_get_sentences(file):
    return file.get_relevant_sentences()

def test_extract_relevant_sentences():
#    outputfile_format="db"
    folder_path = r'C:\\Users\gulsha\Desktop\Articles extra for mining\\'
    main_terms = ["increas", "decreas", "relationship", "correlat", "structur", "fragment", "class", "compound", "molecul", "significant", "high", "affect"]
    relation_words =["toxicit","acute", "LC50", "EC50"]
    n = int(os.cpu_count()/2)
    pdfFileNames = FilesReader.get_file_names(folder_path)
    list_of_articles = [rse.RelevantSentences(item, main_terms, relation_words) for item in pdfFileNames]
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=n) as executor:
        res = executor.map(test_get_sentences, list_of_articles)
    
    assert len(list_of_articles) > 0
    assert res != None
                             
    
    