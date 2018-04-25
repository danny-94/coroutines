def countdown(n):
    print('counting down from',n)
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)