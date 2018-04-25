import time
# from cofollow import follow
from coroutine import coroutine
def follow(thefile,target):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.10)
            continue
        target.send(line)
# A grep filter coroutine
@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)
@coroutine
def printer():
    while True:
        line = (yield)
        print(line)

f = open('input_for_tail')
follow(f, grep('python',printer()))