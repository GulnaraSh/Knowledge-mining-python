
"""
Unit tests for the knowmine_app.OutputfileGenerator module.
"""

from knowmine_app.OutputfileGenerator import Output
import os


folder = os.getcwd()
filename = "Test_file"
result = [filename, "Test sentence is produced",1,1]
result_output = Output (folder, result)

def test_add_result_to_database():
    
    result_output.add_result_to_database()
    
    
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.db') ): 
            result_file_db = 1            
           
    assert result_file_db == 1



def add_result_to_excel():
    
    result_output.add_result_to_excel()
    
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.xlsx') ): 
            result_file_xlsx = 1            
           
    assert result_file_xlsx == 1
    