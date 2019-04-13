foo = 1 #global

def func():
    bar = 2 # local
    print(globals())
    print(locals())

func()