def grades(g):
    return g

user_grades = grades([100,101,99,0,30])

print(user_grades)


def add (a,b):
    return [a+b]

total = add (10,100)
print(total)



name = "John Jay"

def find_j(s,c):
    char_count = 0
    for i in range(len(s)):
        if s[i] == c:
            char_count +=1
    return char_count

# f is the caller of the function
f = find_j(name,'J')

print(f)