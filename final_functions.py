import re
import os
from classes import Question, Answer
from fnmatch import fnmatch
import sys
import glob
import errno
import pathlib


def parse_questions(text_to_search_question, text_to_search_answer, subject, sub_section):
    print('From parse_questions : ')

    print('subject passed is : as below')
    print(subject)
    print('sub_section passed is : as below')
    print(sub_section)

    subject = re.sub(' finished files', '', subject)
    sub_section = re.sub('_finished', '', sub_section)

    #print('subject is as below :')
    # print(subject)
    #print('sub_section is as below :')
    # print(sub_section)
#
    #print('text_to_search_question passed is as below :')
    # print(text_to_search_question)
#
    #print('text_to_search_answer passed is as below :')
    # print(text_to_search_answer)

    position_hits = []
    sep = 'Read the assertion'
    text_to_search_question = text_to_search_question.split(sep, 1)[0]

    pattern = re.compile('\d{3}.[A-Z]')

    matches = pattern.finditer(text_to_search_question)

    for match in matches:
        position_hits.append(match.span())

    question_list = []

    for i in range(0, len(position_hits) - 1):
        start = position_hits[i][0]
        end = position_hits[i + 1][0]
        question = Question(text_to_search_question, start, end, subject, sub_section)
        question_list.append(question)

    position_hits = []

    pattern = re.compile('\d{3}\.+')

    matches = pattern.finditer(text_to_search_answer)

    for match in matches:
        position_hits.append(match.span())

    answer_list = []

    for i in range(0, len(position_hits) - 1):
        # end = position_hits[i + 1][1] - 1

        # scontent = text_to_search[int(start), int(end)]
        start = position_hits[i][0]
        end = position_hits[i + 1][0]
        answer = Answer(text_to_search_answer, start, end)
        answer_list.append(answer)

    for i in range(0, len(question_list)):
        question = question_list[i]
        if question.is_eligible == 1:
            for j in range(0, len(answer_list)):
                answer = answer_list[j]
                if answer.is_eligible == 1:
                    if(question.question_id == answer.answer_id):
                        print('Yes, question_id and answer_id match')
                        question.question_content = re.sub('\d{3}.', '', question.question_content)
                        answer.answer_content = re.sub('\d{3}.', 'Answer = ', answer.answer_content)
                        question.answer_content = answer.answer_content
                        question.answer = answer.answer
                        question.generate_sql()
                        print('Printing final Question SQL as below')
                        print(question.sql)
                        print('\n\n')

               # print(question)

    print('Length of question_list is : ')
    print(len(question_list))
    print('Length of ans_list is : ')
    print(len(answer_list))
