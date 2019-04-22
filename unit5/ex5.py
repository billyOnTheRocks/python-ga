#list comprehension
numbers = [1,2,3,4]

g = [3*x for x in numbers]
print(g)

#same thing in a for loop syntax
g1 = []
for i in numbers:

    g1.append(i*3)

print(g1)


h = [3 * x for x in numbers if x < 2]

print(h)


numbers_two = [1,2,3,4]

j = [[x,x**2] for x in numbers_two]
print(j)