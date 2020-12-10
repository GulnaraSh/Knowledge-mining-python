# -*- coding: utf-8 -*-
"""
Unit tests for the knowmine_app.AllSentencesExtractor module.
"""

from knowmine_app.TextExtractor import TextExtraction


def test_getText():
    
    article = TextExtraction(r"test_article.pdf")
    
    assert article.getText () != None
    assert article.getText () != ''
    
