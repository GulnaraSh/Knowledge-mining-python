Usage
=====

The `knowmine` package provides the :code:`knowmine` import module
allowing to extract relevant sentences to an output file of the chosen format. 
The following formats are currently available: SQLite database "db" or excel "xls". 
Note: if the format of the output file is not specified, a "db" file will be created
by default. 
The type of the extracted knowledge is specified by the list of terms and relation words.
The User should also provide a number of cores used for the process parallelization. 
The defaults value is 2. 

In the example below acute toxicity articles are analyzed to retrieve information 
associated with the increase and prediction of toxicity. 

**General usage:**

.. code-block:: Python

   import knowmine
   
   folder_path = "C:/Acute toxicity articles/"
   main_terms = ["toxicit"]
   relation_words = ["increas", "predict"]
   knowmine.extract_relevant_sentences(folder_path, main_terms, 
                                          relation_words, "xls", cores_number)

**Windows:**

.. code-block:: Python

   import knowmine

   def main():

       folder_path = "C:/Acute toxicity articles/"
       main_terms = ["toxicit"]
       relation_words = ["increas", "predict"]
       knowmine_app.extract_relevant_sentences(folder_path, main_terms,
                                           relation_words, "xls", cores_number)

   if __name__ == '__main__':
    main() 