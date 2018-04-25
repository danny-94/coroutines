# decorator for calling __next__ whenever coroutine is called
def coroutine(func):
    def wrapper(*args,**kwargs):
        f = func(*args,**kwargs)
        f.__next__()
        return f 
    return wrapper

@coroutine
def grep(pattern):
    print('looing for %s pattern'%pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

if __name__ == "__main__":
    g = grep('python')
    g.send('Yeah, but no, but yeah, but no')
    g.send('A series of tubes"')
    g.send('python generators rock!')
    g.close()