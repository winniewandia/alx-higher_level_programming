#!/usr/bin/python3
"""This module contains a script that adds all arguments to a
Python list, and then save them to a file.
Imported load_from_json_file and save_to_json_file and used them
to load and save file.
"""
import sys
import os.path

load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

args_list = []
if os.path.exists("add_item.json"):
    args_list = load("add_item.json")

for args in sys.argv[1:]:
    args_list.append(args)

save(args_list, "add_item.json")
