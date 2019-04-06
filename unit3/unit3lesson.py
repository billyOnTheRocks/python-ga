'''d = {}
#dictionaries
student = {
    "name": "Suresh",
    "age": 25,
    "address": "112 Main street"
}

print(student)

for key, value in student.items()
    print(key, " ", value)
'''

students = {
    1:
        {
            'name': 'John',
            'gpa': 3.0,
            'classes_taken': ('490',)
        },
    2:
        {
            'name': 'Mike',
            'gpa': 2.0,
            'classes_taken': ('CSC211', 'CSC220', 'CSC326',)
        },
    3:
        {
            'name': 'Stacy',
            'gpa': 4.0,
            'Major': 'CS',
            'classes_taken': ('CSC126', 'CSC211', 'CSC326',)
        },
    4:
        {
            'name': 'Bruce',
            'gpa': 3.2,
            'Major': 'CSI',
            'Minor': 'ISI',
            'classes_taken': ('CSC211', 'CSC326',)
        },
    5:
        {
            'name': 'Jane',
            'gpa': 3.7,
            'major': 'CSI',
            'minor': 'ISI',
            'classes_taken': ('CSC126', 'CSC211', 'CSC326', 'CSC330', 'CSC490')
        }
}

#nested for loop to access the dictionaries within the dictionary
for keys, values in students.items():
    for k, v in values.items():
        if k == "gpa" and v >= 3.0:
            print(k," ", v)




