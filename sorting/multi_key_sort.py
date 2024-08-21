student_tuples = [
    ('sanjay', 'B', 16),
    ('vijay', 'B', 17),
    ('ajay', 'A', 16),
]
print(sorted(student_tuples, key=lambda student: student[2]))
print(sorted(student_tuples, key=lambda student: -student[2]))
print(sorted(student_tuples, key=lambda student: student[2], reverse=True))
print(sorted(student_tuples, key=lambda student: (-student[2], student[1])))

'''
output:
[('sanjay', 'B', 16), ('ajay', 'A', 16), ('vijay', 'B', 17)]
[('vijay', 'B', 17), ('sanjay', 'B', 16), ('ajay', 'A', 16)]
[('vijay', 'B', 17), ('sanjay', 'B', 16), ('ajay', 'A', 16)]
[('vijay', 'B', 17), ('ajay', 'A', 16), ('sanjay', 'B', 16)]
'''