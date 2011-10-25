#!/usr/bin/env python

from math import sqrt

import locale
import os
import random
import string
import sys
import subprocess
import tempfile

def gen_randname():
    tempdir = tempfile.gettempdir()
    lenght = 8
    random_name = ''.join(random.choice(string.letters) for i in xrange(lenght))
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
        result = _result.readlines()
        _result.close()
        return result
    else:
        raise RuntimeError(stderr)
    
def stdev(X, average):

    if (len(X) > 1 ):
        summation = 0
        for x in X:
            summation += (long(x) - average)**2         
        return sqrt(summation/long(len(X) - 1))
    else:
        return 0.0

def main(argv):

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    query = select('count(RUNNING)', 'where COMMAND like \'\'mask%\'\' and EXIT_CODE=0')
    patients = long(query[0])

    query = select('count(RUNNING)', 'where COMMAND like \'\'fsl%\'\' and EXIT_CODE=0')
    images = long(query[0])
                 
    condition = 'where EXIT_CODE=0'

    query = select('max(CREATION + QUEUED + DOWNLOAD + RUNNING + UPLOAD)', condition)
    time = float(query[0])

    timespan = time / 60**2
   
    query = select('count(RUNNING)', condition)
    jobs = long(query[0])

    query = select('sum(RUNNING)', condition)
    time = float(query[0])

    cputime = time / 60**2

    query = select('count(RUNNING)')
    count = float(query[0])
    
    rate = (1 - jobs/count)

    print ' {0:7d} \t {1:7d} \t {2:11.3f} \t {3:7n} \t {4:11.3f} \t {5:11.2%}\n'.format(
        patients, images, timespan, jobs, cputime, rate)

    query = select('distinct COMMAND')
    for item in map(str.strip, query):

        application = item.strip('\"')
        appcondition = 'where COMMAND like \'\'' + application + '\'\''
        subquery = select('count(RUNNING)', appcondition)
        count = float(subquery[0])

        subcondition = 'where COMMAND like \'\'' + application + '\'\' and EXIT_CODE=0'

        subquery = select('count(RUNNING)', subcondition)
        jobs = long(subquery[0])

        subquery = select('avg(RUNNING)', subcondition)
        average = float(subquery[0])

        subquery = select('RUNNING', subcondition)
        stda = stdev(subquery, average)

        subquery = select('min(RUNNING)', subcondition)
        minimum = long(subquery[0])

        subquery = select('max(RUNNING)', subcondition)
        maximum = long(subquery[0])

        rate = (1 - jobs/count)

        subquery = select('avg(QUEUED)', appcondition)
        latency = float(subquery[0])

        print '\t{0:<18s}: {1:7d}\t{2:11.3f}\t{3:11.3f}\t{4:11.3f}\t{5:11.3f}\t{6:11.2%}\t{7:11.3f}'.format(
            application, jobs, average / 60, stda / 60.0, minimum / 60.0, maximum / 60.0, rate, latency / 60.0)

    query = select('avg(QUEUED)')
    latency = float(query[0])

    query = select('QUEUED')
    stdl = stdev(query, latency)

    query = select('min(QUEUED)')
    minimum = long(query[0])

    query = select('max(QUEUED)')
    maximum = long(query[0])

    print '\n {0:11.3f} \t {1:11.3f} \t {2:11.3f} \t {3:11.3f}'.format(latency / 60.0, stdl / 60.0, minimum / 60.0, maximum / 60.0)
    
if __name__ == "__main__":
    main(sys.argv[1:])
