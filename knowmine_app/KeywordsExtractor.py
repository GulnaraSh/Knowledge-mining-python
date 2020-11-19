# -*- coding: utf-8 -*-
"""
sentences module 
"""

import pke

def ExtractKeywords(sentences):
    
    keywords =[]
    keywords_strings =[]
       
    separator = ', '
    
    for i in range(len(sentences)):
       
        a = []
        b = []
        # initialize keyphrase extraction model, here TopicRank
        extractor = pke.unsupervised.TopicRank()
        
        # load the content of the document, here document is expected to be in raw
        # format (i.e. a simple text file) and preprocessing is carried out using spacy
        extractor.load_document(input=sentences[i], language='en')
        
        # keyphrase candidate selection, in the case of TopicRank: sequences of nouns
        # and adjectives (i.e. `(Noun|Adj)*`)
        extractor.candidate_selection()
        
        # candidate weighting, in the case of TopicRank: using a random walk algorithm
        try: 
            extractor.candidate_weighting()
        
            # N-best selection, keyphrases contains the 10 highest scored candidates as
            # (keyphrase, score) tuples
            keyphrases = extractor.get_n_best(n=5)
        
            for k,n in keyphrases: a.append(k)
            b = b + [separator.join(a)]
        
            keywords.append(a)
            keywords_strings.append(b)
                    
        except: 
            
            keywords.append(["NO"])
            keywords_strings.append(["NO"])
            
    return keywords_strings


      
