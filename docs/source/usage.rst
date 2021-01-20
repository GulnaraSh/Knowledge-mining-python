Usage
=====

The `knowmine_app` package provides the :code:`knowmine_app` import module
allowing to extract relevant sentences to an output file of the chosen format. 
The following formats are currently available: SQLite database "db" or excel "xls". 
Note: if the format of the output file is not specified, a "db" file will be created
by default. The type of the extracted knowledge is specified by the list of terms and relation words.

In the example below acute toxicity articles are analyzed to retrieve information associated with
the increase and prediction of toxicity. 

**General usage:**

.. code-block:: Python

   import knowmine_app
   
   folder_path = "C:/Acute toxicity articles/"
   main_terms = ["toxicit"]
   relation_words = ["increas", "predict"]
   knowmine_app.extract_relevant_sentences(folder_path, main_terms, 
                                          relation_words, "xls")

**Windows:**

.. code-block:: Python

   import knowmine_app

   def main():

       folder_path = "C:/Users/gulsha/Desktop/Articles extra for mining/"
       main_terms = ["toxicit"]
       relation_words = ["increas", "predict"]
       knowmine_app.extract_relevant_sentences(folder_path, main_terms,
                                           relation_words, "xls")

   if __name__ == '__main__':
    main() 