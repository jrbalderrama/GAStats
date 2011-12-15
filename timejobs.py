#!/usr/bin/env python

from derby import select
from statistics import stdev

query = select('distinct COMMAND')
for item in map(str.strip, query):
    
    application = item.strip('\"')
    appcondition = 'where COMMAND like \'\'' + application + '\'\''
    subquery = select('count(RUNNING)', appcondition)

    count = float(subquery[0])
    
    subcondition = 'where COMMAND like \'\'' + application + '\'\' and EXIT_CODE=0'
    
    subquery = select('count(RUNNING)', subcondition)
    jobs = long(subquery[0])
    
    subquery = select('avg(DOWNLOAD + RUNNING + UPLOAD)', subcondition)
    average = float(subquery[0])
    
#    subquery = select('RUNNING', subcondition)
#    stda = stdev(subquery, average)
    stda = 0
    
    subquery = select('min(RUNNING)', subcondition)
    minimum = long(subquery[0])
    
    subquery = select('max(RUNNING)', subcondition)
    maximum = long(subquery[0])
    
    rate = (1 - jobs/count)
    
    subquery = select('avg(QUEUED)', appcondition)
    latency = float(subquery[0])
    
    print '\t{0:<18s}: {1:7d}\t{2:11.3f}\t{3:11.3f}\t{4:11.3f}\t{5:11.3f}\t{6:11.2%}\t{7:11.3f}'.format(
        application, jobs, average / 60, stda / 60.0, minimum / 60.0, maximum / 60.0, rate, latency / 60.0)
