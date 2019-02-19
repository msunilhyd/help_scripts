import sys
import glob
import errno

path = '/home/linus/tex/*.tex'   
files = glob.glob(path)   
for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
    try:
        with open(name) as f: # No need to specify 'r': this is the default.
            sys.stdout.write(f.read())
        print('name of the file is : ' + name)
        f = open('{}.txt'.format(name), 'wb')
        data=name
        file = open('{0}.txt'.format(data),"w")
        print('hello')

    except IOError as exc:
        if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            raise # Propagate other kinds of IOError.


