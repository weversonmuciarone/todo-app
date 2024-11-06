'''
glob allows you to filter. The example below filters all files with extention .txt

import glob
myfiles = glob.glob("files/*txt")
print(myfiles)
'''
'''
This module creates and output file with the zip extention as a single example

import shutil
shutil.make_archive("output", "zip")
'''
import webbrowser

user_term = input("Enter a search term: ")
webbrowser.open("https://www.google.com/search?q=" + user_term)






