#count no. of items in a sequence

from collections import Counter

cnt = Counter()
for item in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[item] += 1
    
print(cnt)

'''
output:
Counter({'blue': 3, 'red': 2, 'green': 1})
'''