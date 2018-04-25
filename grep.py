def grep(pattern):
    print('looing for %s pattern'%pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

g = grep('python')
g.__next__()
g.send('Yeah, but no, but yeah, but no')
g.send('A series of tubes"')
g.send('python generators rock!')

