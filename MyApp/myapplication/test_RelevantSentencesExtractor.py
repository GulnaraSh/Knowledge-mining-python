# -*- coding: utf-8 -*-
"""
Unit tests for the knowmine_app.AllSentencesExtractor module.
"""

from knowmine_app.RelevantSentencesExtractor import RelevantSentences

<<<<<<< HEAD:MyApp/myapplication/test_RelevantSentencesExtractor.py
words = ["similar", "decreas"]
=======
words = ["similar", "predict"]
>>>>>>> 7953ada41fed76549b3c64d3c79cb5641ee85423:MyApp/test_RelevantSentencesExtractor.py
keys =["toxicit"]


def test_get_relevant_sentences():
    
    text = RelevantSentences(r"test_article1.pdf",keys, words )
    
    assert len(text.get_relevant_sentences()) > 0

