# Script_03.py
# Author: UmarYusuf.com
# Date: 25/01/2022
# Topic: Working with file data types
# ------------------------------

# Python Files
# --------------
# This topic is often threated under the topic: Python File Input and Output
# Python supports many file types including those specifically use in the GIS.

# List of common files used in python and GIS:
# TEXT
# CSV
# Excel
# JSON
# XML
# HTML
# Image files: JPG, PNG, BMP, etc
# PDF


# Two classifications of files;-
# 1) Plaintext files - contain only basic text characters and do not include font, size, or color information. Text files with the .txt extension or Python script files with the .py extension are examples of plaintext files.
# 2) Binary files - are all other file types, such as word processing documents, PDFs, images, spreadsheets, and executable programs.

# Modules use to store any plain python object in a file and then get it back later: pickle, pprint, shelve


# Opening/Closing TEXT Files

# Recall
sourceFile = open('path_to_file.txt', 'w')
print('Hello', file = sourceFile)
sourceFile.close()


path_to_file = r"C:\Users\Yusuf_08039508010\Desktop\DeskTop\GIS Data Processing Scripts\data files\countries_1.txt"

# Method 1....
f = open(path_to_file)
# perform operations on the file
f.close()


# Method 2....
try:
   f = open(path_to_file)
   # perform operations on the file
finally:
   f.close()


# Method 3....
with open(path_to_file) as f:
   # perform operations on the file


# Reading Text File
# read() – read all text from a file into a string. 
# readline() – read the text file line by line and return all the lines as strings.
# readlines() – read all the lines of the text file and return them as a list of strings.



# Writing to Text File
# write() - writes a string in a single line in the text file
# writelines() - writes a list of string to the text file





