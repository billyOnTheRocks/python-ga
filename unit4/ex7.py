a = float(input("first number"))
b = float(input("second number"))

while True:
    try:
        print(a / b)
        break

    except ZeroDivisionError:
        print("unsupported opperation")

    a = float(input("first number"))
    b = float(input("second number"))



