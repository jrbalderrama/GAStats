#!/usr/bin/env python

from derby import select
from statistics import stdev

query = select('count(RUNNING)', 'where COMMAND like \'\'mask%\'\' and EXIT_CODE=0')
patients = long(query[0])

query = select('count(RUNNING)', 'where COMMAND like \'\'fsl%\'\' and EXIT_CODE=0')
images = long(query[0])

condition = 'where EXIT_CODE=0'

query = select('max(END_E)', condition)
timespan = query[0] / 60**2

query = select('UPLOAD-RUNNING', condition)
jobs = len(query)
#print map(lambda x: x / 60**2, query)
cputime = sum(query) / 60**2

query = select('count(RUNNING)')
total = query[0]

rate = (1 - jobs/float(total))

# print '   {0:11.3f}   {1:7n}   {2:11.3f}   {3:11.2%}\n'.format(
#     timespan, jobs, cputime, rate)

print '   {0:7d}   {1:7d}   {2:11.3f}   {3:7n}   {4:11.3f}   {5:11.2%}'.format(
    patients, images, timespan, jobs, cputime, rate)
