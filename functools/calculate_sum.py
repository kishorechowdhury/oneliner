#calculate sum of a list of values

from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 2))
'''
output:
15
17
'''