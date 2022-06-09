#!/usr/bin/python3
"""
    Function load_from_json_file(filename)
"""
import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.isfile(filename):
    file = load_from_json_file(filename)
else:
    file = []
file.extend(sys.argv[1:])
save_to_json_file(file, filename)
