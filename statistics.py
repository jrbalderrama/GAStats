from math import ceil
from math import floor
from math import fsum
from math import sqrt

def mean(X):
    if len(X):
        return fsum(X) / len(X)
    else:
        float('nan')

def stdev(X):
    if (len(X) > 1):
        avg = mean(X)
        summation = map(lambda x: (x - avg)**2, X)
        return sqrt(sum(summation) / len(X))
    else:
        return 0.0

def median(X):
    index = len(X) // 2
    return sorted(X)[index] if (len(X) % 2) else ((sorted(X)[index - 1] + sorted(X)[index]) / 2.0)

def MAD(X):
    _median = median(X)
    absolute = map(lambda x: abs(x - _median), X)
    return median(absolute)

# quartile according to Mendenhall and Sincich
# (1st) lower quartile: L = (1/4)(n+1)
# (3rd) upper quartile: U = (3/4)(n+1)
# http://mathforum.org/library/drmath/view/60969.html
def lower_quartile(X):
    index = (len(X) + 1) / 4.0 - 1
    index = round(index) if (index % 0.5) else ceil(index)
    return sorted(X)[int(index)]

def upper_quartile(X):
    index = 3 * (len(X) + 1) / 4.0 - 1
    index =  round(index) if (index % 0.5) else floor(index)
    return sorted(X)[int(index)]

def IQR(X):
    lq = lower_quartile(X)
    uq = upper_quartile(X)
    return uq - lq

def lower_15IQR(X):
    lower = lower_quartile(X)
    iqr = IQR(X)
    return filter(lambda x: x > lower - 1.5 * iqr, sorted(X))[0]

def upper_15IQR(X):
    upper = upper_quartile(X)
    iqr = IQR(X)
    return filter(lambda x: x < upper + 1.5 * iqr, sorted(X))[-1]
    

# A = [1, 4, 9, 16, 25, 36, 49, 64, 81]

# median = stats.median(A)
# quartile1 = stats.lq(A)
# quartile3 = stats.uq(A)

# print '   {0:11.3f}   {1:11.3f}   {2:11.3f}'.format(median, quartile1, quartile3)

# A = [1, 2, 3, 4, 5, 6, 7, 8]

# median = stats.median(A)
# quartile1 = stats.lq(A)
# quartile3 = stats.uq(A)

# print '   {0:11.3f}   {1:11.3f}   {2:11.3f}'.format(median, quartile1, quartile3)

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# median = stats.median(A)
# quartile1 = stats.lq(A)
# quartile3 = stats.uq(A)

# print '   {0:11.3f}   {1:11.3f}   {2:11.3f}'.format(median, quartile1, quartile3)

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# median = stats.median(A)
# quartile1 = stats.lq(A)
# quartile3 = stats.uq(A)

# print '   {0:11.3f}   {1:11.3f}   {2:11.3f}'.format(median, quartile1, quartile3)

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# median = stats.median(A)
# quartile1 = stats.lq(A)
# quartile3 = stats.uq(A)

# print '   {0:11.3f}   {1:11.3f}   {2:11.3f}'.format(median, quartile1, quartile3)

