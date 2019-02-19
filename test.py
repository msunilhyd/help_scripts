import re

input = '''639.The placement of \(Zn,\) \(Cd\) and \(Hg\) along with \('d'\) block elements
is not proper because

(a)Their \('d'\) orbitals are completely filled

(b)Their \('d'\) orbitals are empty

(c)They do not form complex compounds

(d)They do not form coloured compounds'''

result = re.sub('\'',  '\\\'', input)
print('\n')

result = re.sub('\d{3}\.',''''2019-02-16 00:00:00', 'Chemistry', 'D and F Block', 2,2);INSERT INTO `question`(`question_content`, `a`, `b`, `c`, `d`, `date_posted`, `section`,`sub_section` ,`ans`, `level`) VALUES (''', result)

print(result)

result = re.sub('\(a\)', '\',\'', result)
result = re.sub('\(b\)', '\',\'', result)
result = re.sub('\(c\)', '\',\'', result)
result = re.sub('\(d\)', '\',\'', result)

result = re.sub('\n','', result)
print('\n')
print('final result is : ')
print(result)
