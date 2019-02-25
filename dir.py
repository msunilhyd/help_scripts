import sys
import glob
import errno
import re

path = '/home/linus/tex/*.tex'   
files = glob.glob(path)   
for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
    try:
        with open(name) as f: # No need to specify 'r': this is the default.
            data = f.read()
            result = re.sub('\'',  '\\\'', data)
            result = re.sub('\d{3}\.',''''2019-02-16 00:00:00', 'Chemistry', 'D and F Block', 2,2);INSERT INTO `question`(`question_content`, `a`, `b`, `c`, `d`, `date_posted`, `section`,`sub_section` ,`ans`, `level`) VALUES (''', result)
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


