principal = float(input("principal"))

compound = float(input("compound"))

rate = float(input("rate"))/100

time = float(input("time"))

a = principal*(1.0 + rate/compound)**(compound*time)

print("your accrued amount is", round(a,2))

