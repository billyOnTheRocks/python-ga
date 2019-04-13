try:
    x = int(input("enter a nunber up to 100"))
    if x < 100:
        raise.TypeError(x)
except TypeError:
    print(x "is out of allowed range")
else
    print(x,"is within the allowed range")
