# -*- coding: utf-8 -*-
"""
module files 

Relevant articles to mine the knowledge from
"""

import re
import fitz
import textract
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO    

class TextExtraction:
    
    def __init__(self, filepath):
        self.filepath = filepath

    def getText(self):
        """Class method extracting texts of articles"""
        
        return self.__gettexts()

       
    def __extracttxt1(self):
        """Helper function to extract text by PyMupdf, fastest"""
        
        x = fitz.open(self.filepath)
        ps =''
        pageN = x.pageCount
        for i in range(pageN):
            pages = x.loadPage(i)
            text =''
            text = pages.getText('text')
            ps = ps + text
        return (ps)   
    
    def __extracttxt2(self):
        """Helper function to extract text by pdfminer, slower but handles 
        formats not recongnised by PyMupdf"""
        
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open(self.filepath, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
    
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
    
        text = retstr.getvalue()
    
        fp.close()
        device.close()
        retstr.close()
        return text
    
    def __extracttxt3(self):
        """Helper function to extract text of formats not recognized by 
        PyMupdf and pdfminer"""
        
        text = textract.process(self.filepath, encoding='utf-8')
        return (str(text))
    
    def __ref_remove(self, text):
        """Helper function to remove the References block of articles"""
        
        words = ['Acknowledgements', 'Acknowledgement','ACKNOWLEDGEMENTS','ACKNOWLEDGEMENT'
                 'Reference','References', 'REFERENCE','REFERENCES']
        p=[]
        for w in words:
            if p ==[]: p = [m.start() for m in re.finditer(w, text)]
        
        try:
            if len(p) > 1: t = p[len(p)-1]
            else: t = p[0]
            head, s, tail = text.partition(text[t:t+13])
            return (head)
        except: return (text)
    
    def __head_remove(self, text):
        """Helper function to remove the heading of articles
        (all until the Introduction part)"""
        
        words = ['Introduction','INTRODUCTION']
        p=[]
        for w in words:
            if p ==[]: p = [m.start() for m in re.finditer(w, text)]
        
        try:
            if len(p) > 1: t = p[len(p)-1]
            else: t = p[0]
            head, s, tail = text.partition(text[t:t+13])
            return (tail)
        except: return (text)
    
    def __cleanText(self,text):
        """Helper function to remove the heading and references block of articles"""
        
        txt = self.__ref_remove(text)
        txt = self.__head_remove(txt)
        txt = re.sub('\S*@\S*\s?', '',txt) #remove emails
            
        return txt
    
    def __gettexts (self):
        """Helper function applying text extraction functions"""
       
        text = self.__extracttxt1()
        if text[0:3] =='���':
            try:
                text= self.__extracttxt2()
                       
            except:
                text=self.__extracttxt3()
                text = re.sub(r'\\r\\n', ' ', text)
        
        else: pass        
        
        text = self.__cleanText(text)
        text = re.sub('\n', "", text)
           
        return text
   

#Test
test = TextExtraction(c[0])
text = test.getText()
    
    
