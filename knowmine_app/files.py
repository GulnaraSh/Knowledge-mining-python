# -*- coding: utf-8 -*-
"""
module files 

Relevant articles to mine the knowledge from
"""


import os
import re
import fitz

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


def get_file_names(folder):
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
            pdfFileNames.append(folder + filename)
    return pdfFileNames


def cleanText(txt):
    txt = article.ref_remove(txt)
    txt = article.head_remove(txt)
    #https://regexr.com/
    #removing emails 
    txt = re.sub('\S*@\S*\s?', '', txt)
 
    #Fix the words
    txt = re.sub('-\n', "", txt)
    return txt        


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






def processFile(filename):
        
    doc = fitz.open(filename)
    print("Opened file--- %s seconds ---" % (time.time() - start_time))
    txt = article.extracttxt(doc)
    print("Extracted txt--- %s seconds ---" % (time.time() - start_time))
       
    cleanedText = cleanText(txt)
    
    cleanedSentences = GetAndCleanSentences(cleanedText)
    
    processedFile["KeyWordsOfSentences"] = ExtractKeywords(processedFile["CleanedSentences"])
    
    processedFile["UsefulSentences"] = ExtractUsefulSentences(processedFile["CleanedSentences"], processedFile["KeyWordsOfSentences"] )
    print("Done process--- %s seconds ---" % (time.time() - start_time))
    processResult = (filename, json.dumps(processedFile["CleanedSentences"]), json.dumps(processedFile["KeyWordsOfSentences"]), json.dumps(processedFile["UsefulSentences"]));
    return processResult












folder = 'X:\\Gulnaras mapp\Textmining\WOS\\Aquatic toxicity\\'


c= get_file_names(folder)