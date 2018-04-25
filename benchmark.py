from copipe import grep
from coroutine import coroutine
import timeit
# class implementation of grep
class GrepHandler(object):
    """docstring for GrepHandler."""
    def __init__(self, pattern,target):
        self.pattern = pattern
        self.target = target
    def send(self,line):
        if self.pattern in line: #self look ups slower
            self.target.send(line)# self look ups is slower

@coroutine
def null():
    while True:
        item = (yield)

line = "python is awesome"
p1 = grep('python',null())
p2 = GrepHandler('python',null())
if __name__ == "__main__":
    time1 = timeit.timeit('p1.send(line)','from __main__ import line,p1')
    time2 = timeit.timeit('p2.send(line)','from __main__ import line,p2')
    print('Coroutine method',time1)
    print('Object method',time2)

 
