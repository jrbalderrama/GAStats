#!/usr/bin/env python

import statistics as stats

def select_from_file(archive):
    _result = open(archive, "r")        
    result = map(float, _result.readlines())
    _result.close()
    return result

FACTOR = 60.0

query = select_from_file('queued.dat')

mean = stats.mean(query) / FACTOR
deviation = stats.stdev(query) / FACTOR
minimum = min(query) / FACTOR
maximum = max(query) / FACTOR

median = stats.median(query) / FACTOR
mad = stats.MAD(query) / FACTOR
lower = stats.lower_quartile(query) / FACTOR
upper = stats.upper_quartile(query) / FACTOR

# print '   {0:11.3f}   {1:11.3f}   {2:11.3f}   {3:11.3f}'.format(mean, deviation, minimum, maximum)
# print '   {0:11.3f}   {1:11.3f}   {2:11.3f}   {3:11.3f}'.format(median, mad, lower, upper)

# for latency.tab using FACTOR = 60.0 
print '{0:11.3f}   {1:11.3f}   {2:11.3f}   {3:11.3f}   {4:11.3f}   {5:11.3f}   {6:11.3f}   {7:11.3f}'.format(mean, deviation, minimum, maximum, median, mad, lower, upper) 

# lower_iqr = stats.lower_15IQR(query)
# upper_iqr = stats.upper_15IQR(query)

# ## for latency.dat using FACTOR = 1.0
# print '{0:.0f} {1:.0f} {2:.3f} {3:.0f} {4:.0f}'.format(lower_iqr, lower, median, upper, upper_iqr)
