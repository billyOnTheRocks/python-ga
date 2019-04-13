number_of_students = 1

def add():
    global number_of_students
    number_of_students = number_of_students + 2
    print("inside the add function", number_of_students)

add()
