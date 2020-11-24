# -*- coding: utf-8 -*-
"""
sentences module 
"""

from KeywordsExtractor import ExtractKeywords
import TextExtractor as txtext
import AllSentencesExtractor as allsent
import json 


class RelevantSentences:
        
    def __init__(self,file_name, main_terms,relation_words):
        self.file_name = file_name
        self.main_terms = main_terms
        self.relation_words = relation_words

    def get_relevant_sentences(self):
        """Class method extracting relevant sentences of all the sentences of the texts"""
        
        return self.__ExtractUsefulSentences()

    
    def __sentences_with_terms(self):
        sents = []
        text_obj = txtext.TextExtraction(self.file_name)
        text = text_obj.getText()
        allsents_obj = allsent.SentencesExtraction(text)
        allsentences = allsents_obj.get_sentences()
        
        for sent in allsentences :
            if any(word for word in self.main_terms if(word in sent)):
                sents.append(sent)
        return sents
                
       
    def __ExtractUsefulSentences(self):
        
        sents_with_keys = self.__sentences_with_terms()
        keywords_strings = ExtractKeywords(sents_with_keys)
        sent_to_read = []
            
        for j in keywords_strings:
            if any(word for word in self.main_terms if(word in j[0])) and any(word for word in self.relation_words if(word in j[0])):
                sent_to_read.append(sents_with_keys[keywords_strings.index(j)])
         
        return sent_to_read   



# Finish this part
    def output(self):
        
       processResult = (filename, json.dumps(processedFile["CleanedSentences"]), json.dumps(processedFile["KeyWordsOfSentences"]), json.dumps(processedFile["UsefulSentences"]));
    return processResult

    

words = ["increas", "decreas", "relationship", "correlat", "structur", "fragment", "class", "compound", "molecul", "significant", "high", "affect"]
keys =["toxicit","acute", "LC50", "EC50"]

#Test
test_s = RelevantSentences(allsents, keys,words)
sentences = test_s.get_relevant_sentences()
    
