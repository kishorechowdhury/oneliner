#return list of values based on a given condition

from itertools import takewhile, dropwhile

data = [0, 1, 2, 3, 4]
print(list(takewhile(lambda x: x < 3, data)))
print(list(dropwhile(lambda x: x < 3, data)))

'''
output:
[0, 1, 2]
[3, 4]
'''