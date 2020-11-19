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

def extracttxt1(path):
    x = fitz.open(path)
    ps =''
    pageN = x.pageCount
    for i in range(pageN):
        pages = x.loadPage(i)
        text =''
        text = pages.getText('text')
        ps = ps + text
    return (ps)   

def ref_remove(text):
    words = ['Acknowledgements', 'Acknowledgement','Reference','References', 'REFERENCE','REFERENCES']
    p=[]
    for w in words:
        if p ==[]: p = [m.start() for m in re.finditer(w, text)]
    
    try:
        if len(p) > 1: t = p[len(p)-1]
        else: t = p[0]
        head, s, tail = text.partition(text[t:t+13])
        return (head)
    except: return (text)

def head_remove(text):
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

def cleanText(text):
    txt = ref_remove(text)
    txt = head_remove(txt)
    txt = re.sub('\S*@\S*\s?', '',txt) #remove emails
        
    return txt

def extracttxt3(path):
    text = textract.process(path, encoding='utf-8')
    return (str(text))


def extracttxt2(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
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
    
    
def gettexts (path):
   
    text = extracttxt1(path)
    if text[0:3] =='���':
        try:
            text=extracttxt2(path)
                   
        except:
            text=extracttxt3(path)
            text = re.sub(r'\\r\\n', ' ', text)
    
    else: pass        
    
    text = cleanText(text)
    text = re.sub('\n', "", text)
    
    
    return text
   


t2 =[]
for i in c:
    t2.append(gettexts(i))
    
    
    
