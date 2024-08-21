#most common items in a sequence

from collections import Counter

print(Counter('abracadabra').most_common(3))

'''
output:
[('a', 5), ('b', 2), ('r', 2)]
'''