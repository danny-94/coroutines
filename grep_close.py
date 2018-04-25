from coroutine import croutine 
@coroutine
def grep(pattern):
    print('looking for %s pattern' % pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('Going away, Good bye')

g = grep('python')
g.send('Yeah, but no, but yeah, but no')
g.send('A series of tubes"')
g.send('python generators rock!')
g.throw(RuntimeError,"you're are hosed")
g.close()

