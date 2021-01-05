Usage
=====

The `knowmine_app` package provides the :code:`knowmine_app` import module
allowing to extract relevant sentences to an output file of the chosen format. 
The following formats are currently available: SQLite database "db" or excel "xls".
The type of the extracted knowledge is specified by the list of terms and relation words.

In the example below acute toxicity articles are analyzed to retrieve information associated with
the increase and prediction of toxicity. 

.. code-block:: Python

   import knowmine_app
   
   folder_path = "C:/Acute toxicity articles/"
   main_terms = ["toxicit"]
   relation_words = ["increas", "predict"]
   weather_app.extract_relevant_sentences(folder_path, main_terms, relation_words, outputfile_format="db")
