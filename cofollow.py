import time
from coroutine import coroutine
# A source that mimics the unix tail -f
def follow(thefile,target):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)

# A sink that just prints the lines
@coroutine
def printer():
    while True:
        line = (yield)
        print(line)
if __name__ == "__main__":
    f = open('input_file')
    follow(f,printer())