# -*- coding: utf-8 -*-
"""
Unit tests for the knowmine_app.AllSentencesExtractor module.
"""

from knowmine_app.RelevantSentencesExtractor import RelevantSentences

words = ["similar", "decreas"]
keys =["toxicit"]


def test_get_relevant_sentences():
    
    text = RelevantSentences(r"test_article1.pdf",keys, words )
    
    assert len(text.get_relevant_sentences()) > 0

