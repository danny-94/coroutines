from coroutine import coroutine 
@coroutine
def grep(pattern):
    print('looking for %s pattern' % pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit: # run when g.close() is called
        print('Going away, Good bye')

if __name__ == "__main__":
    g = grep('python')
    g.send('Yeah, but no, but yeah, but no')
    g.send('A series of tubes"')
    g.send('python generators rock!')
    g.close()
    g.throw(RuntimeError,"you're are hosed") #can also throw error

