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
def extract_relevant_sentences(folder_path, main_terms, relation_words, 
                               outputfile_name = "MyProject", outputfile_format = "db"):
    
    
    n = int(os.cpu_count()/2)
    pdfFileNames = FilesReader.get_file_names(folder_path)
    
    
    if outputfile_format == "db":
        args = ((file, main_terms, relation_words) for file in pdfFileNames)
        with concurrent.futures.ProcessPoolExecutor(max_workers=n) as executor:
            res = executor.map(lambda p: f(*p), args)
                
            for result in res:
                conn = of.create_connection('{self.dbname}.db')
                with conn:
                    of.add_result_to_database(conn, result)

    
    if outputfile_format == "txt":
    
    print ('The extraction is finished')
    


#test 
folder_path = 'C:\\Users\gulsha\Desktop\Articles extra for mining\\'

if __name__ == '__main__':
    package.startMining(*)
