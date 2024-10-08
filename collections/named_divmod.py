#example of namedtuple

from collections import namedtuple

def custom_divmod(x, y):
    DivMod = namedtuple('DivMod', ['quotient', 'remainder'])
    return DivMod(*divmod(x, y))
    
result = custom_divmod(12, 5)

print(result.quotient)
print(result.remainder)

'''
output:
2
2
'''