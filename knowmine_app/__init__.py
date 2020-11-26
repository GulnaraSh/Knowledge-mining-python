"""
The knowmine module
======================
The " knowmine app"extracts potentially relevant sentences from the collection of scientific articles.
Currently a User should provide a path to the collection of texts in pdf format and list of keywords for 
the extraction.

"""

import os
import FilesReader
import RelevantSentencesExtractor as rse
import concurrent.futures
import OutputfileGenerator as of





#for many articles
def extract_relevant_sentences(folder_path, main_terms, relation_words, outputfile_format="db"):
    
    
    n = int(os.cpu_count()/2)
    pdfFileNames = FilesReader.get_file_names(folder_path)
    list_of_articles = [rse.RelevantSentences(item, main_terms, relation_words) for item in pdfFileNames]
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=n) as executor:
        res = executor.map(get_sentences, list_of_articles)
    
   
                             
    for result in res:
         if outputfile_format == "db":
             database = of.Output(folder_path,result)
             database.add_result_to_database()

    
         if outputfile_format == "xls":
            
  
             data = of.Output(folder_path,result)
             data.add_result_to_excel()
       
    print ('The extraction is finished')
    



def get_sentences(file):
    return file.get_relevant_sentences()


#test 
folder = 'C:\\Users\gulsha\Desktop\Articles extra for mining\\'

words = ["increas", "decreas", "relationship", "correlat", "structur", "fragment", "class", "compound", "molecul", "significant", "high", "affect"]
keys =["toxicit","acute", "LC50", "EC50"]

if __name__ == '__main__':
    extract_relevant_sentences (folder, keys,words,"db")


