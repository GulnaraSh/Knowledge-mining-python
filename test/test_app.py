# -*- coding: utf-8 -*-
"""
Test for the knowmine main module
"""


import os
from knowmine_app import extract_relevant_sentences


def test_extract_relevant_sentences():
    folder_path = os.getcwd() + "/" 
    main_terms = ["increas", "predict"]
    relation_words =["toxicit"]
    
    extract_relevant_sentences (folder_path, main_terms, relation_words, "db")     
    
    