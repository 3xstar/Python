import time

def hours():
    hour = 0
    start_time = time.time()
    while True:
        yield round((time.time() - start_time) / 3600)

def minutes():
    minute = 0
    start_time = time.time()
    while True:
        yield round((time.time() - start_time) / 60)

def seconds():
    second = 0
    start_time = time.time()
    while True:
        yield round(time.time() - start_time)

h = hours()
m = minutes()
s = seconds()

while True:
    print(next(h), next(m), next(s))