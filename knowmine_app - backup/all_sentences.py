# -*- coding: utf-8 -*-
"""
sentences module 
"""

import re
import spacy

from collections import OrderedDict


nlp = spacy.load('en_core_web_lg')
# extracting sentences     
abbreviations = {'dr.': 'doctor', 'mr.': 'mister', 'bro.': 'brother', 'bro': 'brother', 
                 'mrs.': 'mistress', 'ms.': 'miss', 'jr.': 'junior', 'sr.': 'senior',
                 'i.e.': 'for example', 'e.g.': 'for example', 'vs.': 'versus', 'Fig.': 'Figure', 
                 'www': 'website', 'et al': 'ref', 'et al.': 'ref', 'D.magna':'Daphnia magna'}
terminators = ['.', '!', '?']
wrappers = ['"', "'", ')', ']', '}']


class SentencesExtraction:
    
    def __init__(self, filetext):
        self.filetext = filetext

    def get_sentences(self):
        """Class method extracting all the sentences of article texts"""
        sentences = self.__find_sentences(self.filetext)
        #Remove incomplete sentences
        sentences = self.__remove_incomplete_sent(sentences)
        # Remove extra spaces 
        sentences = self.__remove_extra_spaces(sentences)
        return sentences

    
    def __find_sentences(self):
       end = True
       sentences = []
       paragraph = self.filetext
       while end > -1:
           end = find_sentence_end(paragraph)
           if end > -1:
               sentences.append(paragraph[end:].strip())
               paragraph = paragraph[:end]
       sentences.append(paragraph)
       sentences.reverse()
       return sentences
    
    
    def __find_all(a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1:
                return
            yield start
            start += len(sub)
    
    def __find_sentence_end(self):
        paragraph = self.filetext
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
    
    def __sentences_with_key(all_s,keys):
        sents = []
        for sent in all_s:
            if any(word for word in keys if(word in sent)):
                sents.append(sent)
        return sents
                
    def __remove_ref(all_s):
        full_sent =[]
        for sent in all_s:
            full_sent.append(re.sub(" [\(\[].*?[\)\]]", "", sent))
        return full_sent
        
    def __remove_extra_spaces(all_s):
        full_sent =[]
        for sent in all_s:
            sent = re.sub(r'\s+', ' ', sent)
            sent = re.sub("\n", " ", sent)
            
            full_sent.append(sent)   
        return full_sent
    
    def __remove_incomplete_sent(all_s):
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
    #   sentences = remove_ref(sentences)  
        
        sentences = sentences_with_key(sentences, keys)
        
        return sentences
    
    def ExtractUsefulSentences(all_s, keywords_strings):
            
        sent_to_read = []
            
        for j in keywords_strings:
            if any(word for word in keys if(word in j[0])) and any(word for word in words if(word in j[0])):
                sent_to_read.append(all_s[keywords_strings.index(j)])
         
        return sent_to_read   



    

list_of_sentences = []

for txt in t2:
    list_of_sentences.append(GetAndCleanSentences(txt))
