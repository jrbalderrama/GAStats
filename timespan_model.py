#!/usr/bin/env python

from derby import select
from statistics import stdev

def select_from_file(archive):
    _result = open(archive, "r")        
    result = map(float, _result.readlines())
    _result.close()
    return result

query = select_from_file('shiwa/patients.dat')
patients_shiwa = long(query[0])

query = select_from_file('dirac/patients.dat')
patients_dirac = long(query[0])

query = select_from_file('local/patients.dat')
patients_local = long(query[0])

patients = patients_shiwa + patients_dirac + patients_local

query = select_from_file('shiwa/images.dat')
images_shiwa = long(query[0])

query = select_from_file('dirac/images.dat')
images_dirac = long(query[0])

query = select_from_file('local/images.dat')
images_local = long(query[0])

images = images_shiwa + images_dirac + images_local

query = select_from_file('shiwa/timespan.dat')
timespan_shiwa = query[0] / 60**2
print timespan_shiwa

query = select_from_file('dirac/timespan.dat')
timespan_dirac = query[0] / 60**2
print timespan_dirac

query = select_from_file('local/timespan.dat')
timespan_local = query[0] / 60**2
print timespan_local

timespan = max(timespan_shiwa, timespan_dirac, timespan_local)

query = select_from_file('shiwa/running.dat')
jobs_shiwa = len(query)
cputime_shiwa = sum(query) / 60**2

query = select_from_file('dirac/running.dat')
jobs_dirac = len(query)
cputime_dirac = sum(query) / 60**2

query = select_from_file('local/running.dat')
jobs_local = len(query)
cputime_local = sum(query) / 60**2

jobs = jobs_shiwa + jobs_dirac + jobs_local
cputime = cputime_shiwa + cputime_dirac + cputime_local

query = select_from_file('shiwa/total.dat')
total_shiwa = query[0]

query = select_from_file('dirac/total.dat')
total_dirac = query[0]

query = select_from_file('local/total.dat')
total_local = query[0]

total = total_shiwa + total_dirac + total_local

rate = (1 - jobs/float(total))

# print '   {0:11.3f}   {1:7n}   {2:11.3f}   {3:11.2%}\n'.format(
#     timespan, jobs, cputime, rate)

print '   {0:7d}   {1:7d}   {2:11.3f}   {3:7n}   {4:11.3f}   {5:11.2%}'.format(
    patients, images, timespan, jobs, cputime, rate)
