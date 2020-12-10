# -*- coding: utf-8 -*-
"""
Unit tests for the knowmine_app.AllSentencesExtractor module.
"""

from knowmine_app.RelevantSentencesExtractor import RelevantSentences

words = ["increas", "decreas", "relationship", "correlat", "structur", "fragment", "class", "compound", "molecul", "significant", "high", "affect"]
keys =["toxicit","acute", "LC50", "EC50"]


def test_get_relevant_sentences():
    
    text = RelevantSentences(r"test_article.pdf",keys, words )
    
    assert len(text.get_relevant_sentences()) > 0

