import re
import os
from classes import Question, Answer
from final_functions import parse_questions
from fnmatch import fnmatch
import sys
import glob
import errno
import pathlib


root = '/home/linus/Downloads/j-given-tex/Chemistry finished files'
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
                my_list.append(subject_name)
                my_list.append(subsection_name)
                my_list.append(folder_path)
                section_name_map[subsection_name] = list(dict.fromkeys(my_list).keys())
                #print('printing my_list')
                # print(my_list)
                #print('subject_name is : ')
                # print(subject_name)
                #print('subsection_name is : ')
                # print(subsection_name)

# print('section_name_map.keys(\n\n')
# print(section_name_map.keys())
#print('section_name_map.items() \n\n')
# print('\n\n')
# print(section_name_map.items())


final_map = {}
for key in section_name_map.keys():
    value_list = section_name_map.get(key)
    #print('Printing removed duplicate list')
    # print(value_list)
    for value in value_list:
        if "Objective Test" in value:
            if "Answer Key" not in value:
                # print(value)
                final_value = final_map.get(key)
                if final_value is None:
                    final_value = []
                    # print('\n')
                final_value.append(value)
                final_map[key] = final_value
    #print('From removed Duplicates')
    # print(value_list[0])
    # print(value_list[1])
    final_value.append(value_list[0])
    final_value.append(value_list[1])


#print('Printing final_map below :')
# print(final_map)

for key in final_map.keys():
    list_value = final_map.get(key)
    #print('Printing list_value as below')
    # print(list_value)
    if(len(list_value) < 2):
        print('list_value len is less than 2')
    sub_section = list_value[len(list_value) - 1]
    subject = list_value[len(list_value) - 2]
    text_to_search_question = ''
    text_to_search_answer = ''
    for value in list_value:
        #print('Printing complete value as below :')
        # print(value)
        if '/Objective Test/Questions/' in value or '/Objective Test/Question Paper/' in value:
            #print('Printing value as below : /Questions/ or /Question Paper/ exists for below :')
            # print(value)
            #print('Yes, value contains /Questions/')
            with open(value, 'r') as f:
                final_question = f.read()
                text_to_search_question += final_question
                f.close()
        elif '/Objective Test/Solutions/' in value or '/Objective Test/Solution/' in value:
            print('Yes, value contains /Solution/')
            with open(value, 'r') as f:
                final_answer = f.read()
                text_to_search_answer += final_answer
                f.close()
    parse_questions(text_to_search_question, text_to_search_answer, subject, sub_section)
