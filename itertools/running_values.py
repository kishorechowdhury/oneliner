#running values of a list of values

from itertools import accumulate
from operator import mul, add

data = [1, 3, 2, 0, 4]
print(list(accumulate(data, max)))
print(list(accumulate(data, mul)))
print(list(accumulate(data, add)))

'''
output:
[1, 3, 3, 3, 4]
[1, 3, 6, 0, 0]
[1, 4, 6, 6, 10]
'''