import os
from fnmatch import fnmatch
import sys
import glob
import errno
import re
import pathlib


root = '/home/linus/tex/main_tex'
pattern = "*.tex"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            section_path = pathlib.PurePath(os.path.join(path, name))
            section_name = str(section_path.parent.parent.parent.parent.name)
            subject_name = str(section_path.parent.parent.parent.parent.parent.name)
            print('section_name is ' + section_name)
            print('subject_name is ' + subject_name)
            
            path_secondary = os.path.join(path, name)
            files = glob.glob(path_secondary)
            section = name
            for name in files:
            	try:
            		with open(name) as f:
            			data = f.read()
            			result = re.sub('\'',  '\\\'', data)
            			result = re.sub('\d{3}\.',''''2019-02-16 00:00:00', \'''' + subject_name+ '''',\'''' + section_name + '''\', 2,2);INSERT INTO `question`(`question_content`, `a`, `b`, `c`, `d`, `date_posted`, `section`,`sub_section` ,`ans`, `level`) VALUES (\'''', result)
            			result = re.sub('\(a\)', '\',\'', result)
            			result = re.sub('\(b\)', '\',\'', result)
            			result = re.sub('\(c\)', '\',\'', result)
            			result = re.sub('\(d\)', '\',\'', result)
            			result = re.sub('\n','', result)

            			result = re.sub('INSERT','\n\nINSERT', result)
            			print('name of the file is : ' + name)
            			f = open('{}.txt'.format(name), 'wb')
            			data=name
            			file = open('{0}.txt'.format(data),"w")
            			file.writelines(result)
            			file.close()
            			print('hello')
            	except IOError as exc:
            		if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            			raise # Propagate other kinds of IOError.



