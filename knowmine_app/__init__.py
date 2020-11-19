"""
The knowmine module
======================
The " knowmine app"extracts potentially relevant sentences from the collection of scientific articles.
Currently a User should provide a path to the collection of texts in pdf format and list of keywords for 
the extraction.

"""

import os
import FilesReader
import RelevantSentencesExtractor

#for many articles
def extract_relevant_sentences(folder_path, main_terms, relation_words, 
                               outputfile_name = "MyProject", outputfile_format = "db"):
    
    
    n = int(os.cpu_count()/2)
    pdfFileNames = FilesReader(folder_path)
    
    if outputfile_format == "db":
        
        with concurrent.futures.ProcessPoolExecutor(max_workers=n) as executor:
            res = executor.map(RelevantSentences.get_relevant_sentences, pdfFileNames)
                
                for result in res:
                    conn = self.__create_connection('{self.dbname}.db')
                    with conn:
                        self.__add_result_to_database(conn, result)
    
    print ('The extraction is finished')
    
