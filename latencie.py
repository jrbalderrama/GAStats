#!/usr/bin/env python

from derby import select
from statistics import stdev

query = select('QUEUED')

latency = mean(query)
stdl = stdev(query)
minimum = min(query)
maximum = max(query)

print '   {0:11.3f}   {1:11.3f}   {2:11.3f}   {3:11.3f}'.format(latency / 60.0, stdl / 60.0, minimum / 60.0, maximum / 60.0)

