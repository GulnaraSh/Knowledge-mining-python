# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:14:42 2019

@author: gulsha
"""

#Relevant sentences extraction
# Development test
import fitz 
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as esw
import pandas as pd

import sqlite3
from sqlite3 import Error
import json 

import re
import numpy as np
import pandas as pd
from pprint import pprint
import concurrent.futures

import time

# spacy for lemmatization
import spacy

# Enable logging for gensim - optional
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)


import nltk
nltk.download('punkt')


import string

from collections import OrderedDict

import re
import pke

punctuations = string.punctuation
start_time = time.time()

results = []

# Adding extra words to stops words list
stopWords = ["fig", "figure", "et", "al.", "table",  
        "data", "analysis", "analyze", "study",  
        "method", "result", "conclusion", "author",  
        "find", "found", "show", "perform",  
        "demonstrate", "evaluate", "discuss", "google", "scholar",   
        "pubmed",  "web", "science", "crossref", "supplementary", "mg", "/l", "ml", "cis", "ppb", "ph", "elsevier", "www", "com","however","The"] + list(esw)

nlp = spacy.load('en_core_web_lg')

for word in stopWords:
    lexeme = nlp.vocab[word]
    lexeme.is_stop = True
    
class article:
    def extracttxt(self):
        ps =''
        pageN = self.pageCount
        for i in range(pageN):
            pages = self.loadPage(i)
            text =''
            text = pages.getText('text')
            ps = ps + text
        return (ps)   
    
    def ref_remove(self):
        p = [m.start() for m in re.finditer('Reference', self)]
        try:
            if len(p) > 1: t = p[len(p)-1]
            else: t = p[0]
            head, s, tail = self.partition(self[t:t+13])
            return (head)
        except: return (self)
    
    def head_remove(self):
        p = [m.start() for m in re.finditer('Introduction', self)]
        try:
            if len(p) > 1: t = p[len(p)-1]
            else: t = p[0]
            head, s, tail = self.partition(self[t:t+13])
            return (tail)
        except: return (self)

# extracting sentences     
abbreviations = {'dr.': 'doctor', 'mr.': 'mister', 'bro.': 'brother', 'bro': 'brother', 'mrs.': 'mistress', 'ms.': 'miss', 'jr.': 'junior', 'sr.': 'senior',
                 'i.e.': 'for example', 'e.g.': 'for example', 'vs.': 'versus', 'Fig.': 'Figure', 'www': 'website', 'et al': 'ref', 'et al.': 'ref'}
terminators = ['.', '!', '?']
wrappers = ['"', "'", ')', ']', '}']


def find_sentences(paragraph):
   end = True
   sentences = []
   while end > -1:
       end = find_sentence_end(paragraph)
       if end > -1:
           sentences.append(paragraph[end:].strip())
           paragraph = paragraph[:end]
   sentences.append(paragraph)
   sentences.reverse()
   return sentences

def find_sentence_end(paragraph):
    [possible_endings, contraction_locations] = [[], []]
    contractions = abbreviations.keys()
    sentence_terminators = terminators + [terminator + wrapper for wrapper in wrappers for terminator in terminators]
    for sentence_terminator in sentence_terminators:
        t_indices = list(find_all(paragraph, sentence_terminator))
        possible_endings.extend(([] if not len(t_indices) else [[i, len(sentence_terminator)] for i in t_indices]))
    for contraction in contractions:
        c_indices = list(find_all(paragraph, contraction))
        contraction_locations.extend(([] if not len(c_indices) else [i + len(contraction) for i in c_indices]))
    possible_endings = [pe for pe in possible_endings if pe[0] + pe[1] not in contraction_locations]
    if len(paragraph) in [pe[0] + pe[1] for pe in possible_endings]:
        max_end_start = max([pe[0] for pe in possible_endings])
        possible_endings = [pe for pe in possible_endings if pe[0] != max_end_start]
    possible_endings = [pe[0] + pe[1] for pe in possible_endings if sum(pe) > len(paragraph) or (sum(pe) < len(paragraph) and paragraph[sum(pe)] == ' ')]
    end = (-1 if not len(possible_endings) else max(possible_endings))
    return end

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)

        

def cleanText(txt):
    txt = article.ref_remove(txt)
    txt = article.head_remove(txt)
    #https://regexr.com/
    #removing emails 
    txt = re.sub('\S*@\S*\s?', '', txt)
 
    #Fix the words
    txt = re.sub('-\n', "", txt)
    return txt

def sentences_with_key(all_s,keys):
    sents = []
    for sent in all_s:
        if any(word for word in keys if(word in sent)):
            sents.append(sent)
    return sents

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
#    sentences = remove_ref(sentences)  
#    sentences = sentences_with_key(sentences, keys)
    
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


def processFile(filename):
    processedFile =	{
      "filename": filename
    }
    
    doc = fitz.open(filename)
    print("Opened file--- %s seconds ---" % (time.time() - start_time))
    txt = article.extracttxt(doc)
    print("Extracted txt--- %s seconds ---" % (time.time() - start_time))
       
    cleanedText = cleanText(txt)
    
    processedFile["CleanedSentences"] = GetAndCleanSentences(cleanedText)
    
    processedFile["KeyWordsOfSentences"] = ExtractKeywords(processedFile["CleanedSentences"])
    
    processedFile["UsefulSentences"] = ExtractUsefulSentences(processedFile["CleanedSentences"], processedFile["KeyWordsOfSentences"] )
    print("Done process--- %s seconds ---" % (time.time() - start_time))
    processResult = (filename, json.dumps(processedFile["CleanedSentences"]), json.dumps(processedFile["KeyWordsOfSentences"]), json.dumps(processedFile["UsefulSentences"]));
    return processResult

def add_result_to_database(conn, result):
    sql = ''' INSERT INTO ANALYSED_SENTENCES(Path, CleanedSentences, KeyWordsOfSentences, UsefulSentences)
              VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, result)
    conn.commit()    



words = ["increas", "decreas", "relationship", "correlat", "structur", "fragment", "class", "compound", "molecul", "significant", "high", "affect"]
keys =["toxicit","acute", "LC50", "EC50"] 
    

#for one exemplary article 
#result = processFile("53.pdf")



#for many articles
def main():
    
    print("--- %s seconds ---" % (start_time))
    path = 'F:\\Test\\'
    database = r"C:\Test\TestDatabase.db"
    
    folder = os.fsencode(path)
    
    pdfFileNames = []
    
    # Get pdf fileName in folder
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.pdf') ): 
            # Do it directly, not using multiple threads: Uncomment below row
            #result = processFile(path + filename)
            #conn = create_connection(database)
            #with conn:
            #    add_result_to_database(conn, result)            
            # REMOVE ABOVE ROWS WHEN NOT DEBUGGING
            pdfFileNames.append(path + filename)
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
            res = executor.map(processFile, pdfFileNames)
            
            for result in res:
                conn = create_connection(database)
                with conn:
                    add_result_to_database(conn, result)
                            
    
    print("--- %s seconds ---" % (time.time() - start_time))
    
if __name__ == '__main__':
    main()