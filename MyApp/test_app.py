# -*- coding: utf-8 -*-
"""
Test for the knowmine main module
"""


import os
import knowmine_app.RelevantSentencesExtractor as rse
import concurrent.futures


def test_get_sentences(file):
    return file.get_relevant_sentences()

def test_extract_relevant_sentences():
#    outputfile_format="db"
    main_terms = ["similar", "predict"]
    relation_words =["toxicit"]
    n = int(os.cpu_count()/2)
    pdfFileNames = [r"test_article1.pdf", r"test_article2.pdf"]
    list_of_articles = [rse.RelevantSentences(item, main_terms, relation_words) for item in pdfFileNames]
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=n) as executor:
        res = executor.map(test_get_sentences, list_of_articles)
    
    assert len(list_of_articles) > 0
    assert res != None
                             
    
    