#!/usr/bin/python

'''
This script use for print all file content recursively inside folder like

dir1/file1
-----------------------
file content

dir1/file2
-----------------------
file content

usage -> print-all folder-name
'''

import os
import sys

# traverse root directory, and list directories as dirs and files as files
def walk_dir(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            filename = os.path.join(root,file)
            print filename
            print('--------------------------------------------')
            with open(filename, 'r') as fin:
                print fin.read()
            print
            print

if len(sys.argv) < 2:
    print('try -> print-all d:/bin')
else:
    walk_dir(sys.argv[1])