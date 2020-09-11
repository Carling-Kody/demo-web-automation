from pylenium import Pylenium
import os
import time


def test_upload_file(py: Pylenium, project_root):
    py.visit('https://demoqa.com/upload-download')
    py.get('#uploadFile').type(f'{project_root}/conftest.py')
    assert py.get('#uploadedFilePath').should().contain_text('conftest.py')


def test_download_file(py):
    file_name = 'sampleFile.jpeg'
    py.visit('https://demoqa.com/upload-download')
    py.get('#downloadButton').click()
    assert wait_for_file_to_exist('/Users/kodycarling/Downloads')


def wait_for_file_to_exist(file_path, timeout=5):
    attempts = 0
    while attempts < timeout:
        if os.path.exists(file_path):
            return True
        time.sleep(1)
        attempts += 1
    return False
