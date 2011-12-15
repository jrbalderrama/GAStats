import os
import random
import string
import subprocess
import tempfile
import sys

def gen_randname():
    tempdir = tempfile.gettempdir()
    length = 8
    random_name = ''.join(random.choice(string.letters) for index in xrange(length))
    return os.path.join(tempdir, random_name) + '.dat'

def connect(database, table, query, condition = '', archive = 'query.dat'):
    script = "protocol \'jdbc:derby:\';" 
    script += "connect \'"+ database + "\';"
    script += "readonly on;"
    script += "CALL SYSCS_UTIL.SYSCS_EXPORT_QUERY (\'select "
    script += query + " from " + table + " " + condition + " \',\'"
    script += archive + "',null,null,null);"
    return script

def select(query, condition = ''):
    database = 'jobs.db'    
    table = 'jobs'
    output = gen_randname()
    statement = connect(database, table, query, condition, output)
    command = ['echo', statement]
    echo = subprocess.Popen(command, stdout=subprocess.PIPE)
    process = subprocess.Popen('ij',
                               stdin=echo.stdout,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)    
    echo.stdout.close()
    stdout, stderr = process.communicate()
    code = process.returncode
    if (code == 0):
        _result = open(output, "r")        
#        result = _result.readlines()
        result = map(float, _result.readlines())
        _result.close()
        return result
    else:
        raise RuntimeError(stderr)

if __name__ == "__main__":
    main(sys.argv[1:])
