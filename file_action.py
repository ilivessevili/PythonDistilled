#!/usr/bin/env python

"""
collection of file actions(read, write, append)

"""
import os

def write_file(file_path,content=None,mode='w'):
    """ write a file using with syntax sugar """
    with open(file_path,mode) as f:
        f.write(content)
        
def read_file(file_path,mode='r'):
    """ read a file into variable """

    content = None
    if os.path.exists(file_path):
        with open(file_path,mode) as f:
            content = f.read()
            return content
    
if __name__ == '__main__':
    write_file('test.txt','this is a test','w')
    print(read_file('test.txt'))
