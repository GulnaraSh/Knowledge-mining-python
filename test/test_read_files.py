"""
Unit tests for the knowmine_app.read_files module
"""
from knowmine_app.read_files import get_file_names

folder = 'C:\\Users\gulsha\Desktop\Articles extra for mining\\'




def test_get_file_names():
    """
    Obtain the files for mining from a specific folder and assert that
   the list of files is non-empty.
    """
    folder = 'C:\\Users\gulsha\Desktop\Articles extra for mining\\'
    
    files_list = get_file_names(folder)
    assert len(files_list) > 0
    
