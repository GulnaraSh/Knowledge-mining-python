# -*- coding: utf-8 -*-
"""
sentences module 
"""

import re

def remove_ref(all_s):
    full_sent =[]
    for sent in all_s:
        full_sent.append(re.sub(" [\(\[].*?[\)\]]", "", sent))
    return full_sent
    
def remove_extra_spaces(all_s):
    full_sent =[]
    for sent in all_s:
        sent = re.sub(r'\s+', ' ', sent)
        sent = re.sub("\n", " ", sent)
        
        full_sent.append(sent)   
    return full_sent

def remove_incomplete_sent(all_s):
    full_sent =[]
   
    for sent in all_s:
        doc = nlp(sent)
        for sent_1 in doc.sents:
              
            has_noun = 2
            has_verb = 1
            for token in sent_1:
                if token.pos_ in ["NOUN", "PRON"]:
                    has_noun -= 1
                elif token.pos_ == "VERB":
                    has_verb -= 1
            if has_noun < 1 and has_verb < 1:
                full_sent.append(sent)
               
                
    full_sent = list(OrderedDict.fromkeys(full_sent)) #removes duplicates
     
    return full_sent
        
        
def GetAndCleanSentences(txt):
    
    sentences = find_sentences(txt)
    #Remove incomplete sentences
    sentences = remove_incomplete_sent(sentences)
    # Remove extra spaces 
    sentences = remove_extra_spaces(sentences)

    # Remove references # not perfect, removes all the things in () and []
    sentences = remove_ref(sentences)  
    
    return sentences


def ExtractKeywords(s):
    
    keywords =[]
    keywords_strings =[]
       
    separator = ', '
    
    for i in range(len(s)):
       
        a = []
        b = []
        # initialize keyphrase extraction model, here TopicRank
        extractor = pke.unsupervised.TopicRank()
        
        # load the content of the document, here document is expected to be in raw
        # format (i.e. a simple text file) and preprocessing is carried out using spacy
        extractor.load_document(input=s[i], language='en')
        
        # keyphrase candidate selection, in the case of TopicRank: sequences of nouns
        # and adjectives (i.e. `(Noun|Adj)*`)
        extractor.candidate_selection()
        
        # candidate weighting, in the case of TopicRank: using a random walk algorithm
        try: 
            extractor.candidate_weighting()
        
            # N-best selection, keyphrases contains the 10 highest scored candidates as
            # (keyphrase, score) tuples
            keyphrases = extractor.get_n_best(n=6)
        
            for k,n in keyphrases: a.append(k)
            b = b + [separator.join(a)]
        
            keywords.append(a)
            keywords_strings.append(b)
                    
        except: 
            
            keywords.append(["NO"])
            keywords_strings.append(["NO"])
            
    return keywords_strings


def ExtractUsefulSentences(all_s, keywords_strings):
        
    sent_to_read = []
        
    for j in keywords_strings:
        if any(word for word in keys if(word in j[0])) and any(word for word in words if(word in j[0])):
            sent_to_read.append(all_s[keywords_strings.index(j)])
     
    return sent_to_read    



