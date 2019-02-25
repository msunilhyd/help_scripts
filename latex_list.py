import os
from fnmatch import fnmatch
import sys
import glob
import errno
import re
import pathlib


root = '/home/linus/Downloads/j-given-tex'
pattern = "*.tex"

question_folder_list = []
answer_folder_list = []
file_name_list = []

section_name_list = []
section_name_map = {}
section_list = []

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            file_name = name
            file_name_list.append(file_name)
            section_path = pathlib.PurePath(os.path.join(path, name))
            section_name = str(section_path.parent.parent.parent.parent.name)
            subject_name = str(section_path.parent.parent.parent.parent.parent.name)
            folder_path = str(section_path)
            # print('section_name is ' + section_name)
            # print('subject_name is ' + subject_name)
            # print('folder_path is ' + folder_path)
            subsection_name = section_name

            if subsection_name in folder_path:
                my_list = section_name_map.get(subsection_name)
                if my_list is None:
                    my_list = []
                print('First printing folder_path')
                print(folder_path)
                print('Yes Objective Test exists')
                my_list.append(folder_path)
                section_name_map[subsection_name] = my_list
                print('printing my_list')
                print(my_list)
                print('subsection_name is : ')
                print(subsection_name)

print('section_name_map.keys(\n\n')
print(section_name_map.keys())
print('section_name_map.items() \n\n')
print('\n\n')
print(section_name_map.items())


final_map = {}
for key in section_name_map.keys():
    print('key is : ')
    print(key)
    print('value is : ')

    value_list = section_name_map.get(key)
    for value in value_list:
        if "Objective Test" in value:
            if "Answer Key" not in value:
                print(value)
                final_value = final_map.get(key)
                if final_value is None:
                    final_value = []
                    print('\n')
                final_value.append(value)
                final_map[key] = final_value

print('Printing final_map below :')
print(final_map)

list_value = final_map.get('VECTOR ALGEBRA_finished')
print('Printing list_value as below')
print(list_value)
