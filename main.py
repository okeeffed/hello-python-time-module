import time
import datetime

print(time.__name__)
print(time.time())

# Getting the local time
print(time.localtime())
print(time.gmtime())
print(time.asctime(time.localtime()))

# Formatting and parsing
print(time.strptime("30 Nov 00", "%d %b %y"))
print(time.strftime("%m/%d/%Y, %H:%M:%S"))
print(time.asctime(time.localtime()))

# Sleep
print('Sleeping for 1s')
time.sleep(1)
print('Sleep complete')

# Comparing times

# Check time now is less than 1 second later
res_one = datetime.datetime.fromtimestamp(time.time()) < datetime.datetime.now() + datetime.timedelta(seconds=1) # True
print(res_one)

# Check time now is after 1 second before
res_two = datetime.datetime.fromtimestamp(time.time()) < datetime.datetime.now() - datetime.timedelta(seconds=1) # False
print(res_two)
