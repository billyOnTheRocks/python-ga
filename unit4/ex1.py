def foo(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


def main():
    foo("hi",10,20,30, total=(input("total")), milk=4.99, chips=1.99)


if __name__=='__main__':
   main()
