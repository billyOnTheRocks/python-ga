import datetime

time = datetime.datetime.now()
print(type(time))

print('weekday short version', time.strftime("%a"))
print('weekday full version',time.strftime("%a"))
