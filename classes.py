import re
import os


class Question:

    def __init__(self, text_to_search, start, last, subject, sub_section):

        question_content = text_to_search[start:last];
        question_content = re.sub('\'', '\\\'', question_content)
        question_content = re.sub('\`', '\\\`', question_content)
        question_content = question_content.replace('\\', '\\\\')
        question_content = re.sub('\(\\textbf.+\d{4}.+', 'DELETED', question_content)
        question_content = re.sub('\\\\DELETED', '', question_content)
        question_content = question_content.replace('\n', '').replace('\r', '')
        question_content = re.sub('\[.*\d{4}\]', '', question_content)
        self.question_content = question_content
        self.question_id = text_to_search[start:start + 3]
        self.level = 2
        section = re.sub('_finished files', '', subject)
        sub_section = re.sub('_finished', '', sub_section)

        self.section = subject
        self.sub_section = sub_section
        position_hits = []
        pattern = re.compile('includegraphics')
        matches = pattern.finditer(question_content)
        for match in matches:
            position_hits.append(match.span())

        if(len(position_hits) > 0):
            self.is_eligible = 0
            return
            print('From Questions :')
            print('len of position_hits is :')
            print(len(position_hits))
            print('\n\n')
            print('Printing position_hits as below :')
            print(position_hits)
            image_start = position_hits[0][0]
            image_end = position_hits[0][1]
            image_file = question_content[image_start:image_end];
            print('Images file is : ')
            print(image_file)
            print('\n\n')
            x = text_to_search.split("{")
            print(x[1].replace('}', ''))
        else:
            self.is_eligible = 1

        option_grp_list = []
        option_span_list = []

        pattern = re.compile('\(a\)')
        matches = pattern.finditer(self.question_content)
        for match in matches:
            option_grp_list.append(match.group())
            option_span_list.append(match.span())

        pattern = re.compile('\(b\)')
        matches = pattern.finditer(self.question_content)

        for match in matches:
            option_grp_list.append(match.group())
            option_span_list.append(match.span())

        pattern = re.compile('\(c\)')
        matches = pattern.finditer(self.question_content)

        for match in matches:
            option_grp_list.append(match.group())
            option_span_list.append(match.span())

        pattern = re.compile('\(d\)')
        matches = pattern.finditer(self.question_content)

        for match in matches:
            option_grp_list.append(match.group())
            option_span_list.append(match.span())

        if len(option_span_list) < 3:
            self.option_a = ''
            self.option_b = ''
            self.option_c = ''
            self.option_d = ''
            self.answer_content = ""
            self.answer = ""
            return
        span_a = option_span_list[0]
        span_b = option_span_list[1]
        if len(option_span_list) < 3:
            span_c = ''
        else:
            span_c = option_span_list[2]
        if len(option_span_list) < 4:
            span_d = ''
        else:
            span_d = option_span_list[3]

        self.option_a = self.question_content[span_a[0]:span_b[0]]
        self.option_b = self.question_content[span_b[0]:span_c[0]]
        if len(option_span_list) < 3:
            return
            self.option_b = self.question_content[span_b[0]:last]
            self.option_c = ''
        else:
            self.option_b = self.question_content[span_b[0]:span_c[0]]
            self.option_c = self.question_content[span_c[0]:last]
        if len(option_span_list) < 4:
            self.option_c = self.question_content[span_c[0]:last]
            self.option_d = ''
        else:
            self.option_c = self.question_content[span_c[0]:span_d[0]]
            self.option_d = self.question_content[span_d[0]:last]
        self.answer_content = ""
        self.answer = ""

        self.question_content = re.sub('\(a\).*', '', self.question_content)

    def __repr__(self):
        if self.is_eligible == 1:
            return '\n ID : {} \n Question : {} \n a : {}\n b : {}\n c : {}\n d : {} \n  \n answer_content : {} \n answer : {} \n is_eligible : {} \n'.format(self.question_id, self.question_content, self.option_a, self.option_b, self.option_c, self.option_d, self.answer_content, self.answer, self.is_eligible)
        else:
            return ''

    def generate_sql(self):
        sql = 'INSERT INTO `question`(`section`, `question_content`, `a`, `b`, `c`, `d`, `ans`, `sub_section`, `level`, `solution`, `date_posted`) VALUES (\'[value-1]\',\'[value-2]\',\'[value-3]\',\'[value-4]\',\'[value-5]\',\'[value-6]\',\'[value-7]\',\'[value-8]\',\'[value-9]\',\'[value-10]\',CURRENT_TIMESTAMP);'
        sql = sql.replace('[value-1]', self.section)
        sql = sql.replace('[value-2]', self.question_content)
        sql = sql.replace('[value-3]', self.option_a)
        sql = sql.replace('[value-4]', self.option_b)
        sql = sql.replace('[value-5]', self.option_c)
        sql = sql.replace('[value-6]', self.option_d)
        sql = sql.replace('[value-7]', str(self.answer))
        sql = sql.replace('[value-8]', self.sub_section)
        sql = sql.replace('[value-9]', str(self.level))
        sql = sql.replace('[value-10]', self.answer_content)

        self.sql = sql


class Answer:

    def __init__(self, text_to_search, start, last):
        answer_content = text_to_search[start:last];
        answer_content = re.sub('\'', '\\\'', answer_content)
        answer_content = re.sub('\`', '\\\`', answer_content)
        answer_content = answer_content.replace('\\', '\\\\')
        answer_content = re.sub('\(\\textbf.+\d{4}.+', 'DELETED', answer_content)
        answer_content = re.sub('\\\\DELETED', '', answer_content)
        answer_content = answer_content.replace('\n', '').replace('\r', '')
        position_hits = []
        pattern = re.compile('includegraphics')
        matches = pattern.finditer(answer_content)
        for match in matches:
            position_hits.append(match.span())

        if(len(position_hits) > 0):
            self.is_eligible = 0
            return
            print('From Questions :')
            print('len of position_hits is :')
            print(len(position_hits))
            print('\n\n')
            print('Printing position_hits as below :')
            print(position_hits)
            image_start = position_hits[0][0]
            image_end = position_hits[0][1]
            image_file = question_content[image_start:image_end];
            print('Images file is : ')
            print(image_file)
            print('\n\n')
            x = text_to_search.split("{")
            print(x[1].replace('}', ''))
        else:
            self.is_eligible = 1
        self.answer_content = answer_content
        self.answer_id = text_to_search[start:start + 3]
        answer_var = text_to_search[start + 5:start + 8]
        self.answer = ''
        if(answer_var == '(a)'):
            self.answer = 1
        if(answer_var == '(b)'):
            self.answer = 2
        if(answer_var == '(c)'):
            self.answer = 3
        if(answer_var == '(d)'):
            self.answer = 4

    def __repr__(self):
        return '\n ID : {} \n Answer {} \n'.format(self.answer_id, self.answer_content)
