# sorted() accepts a reverse parameter with a boolean value. This is used to flag descending sorts.


from operator import itemgetter

student_tuples = [
    ('sanjay', 'A', 16),
    ('vijay', 'B', 17),
    ('ajay', 'B', 15),
]
print(sorted(student_tuples, key=itemgetter(2), reverse=True))


'''
output:
[('vijay', 'B', 17), ('sanjay', 'A', 16), ('ajay', 'B', 15)]
'''