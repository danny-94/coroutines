def countdown(n):
    print('counting down from',n)
    while n>=0:
        newvalue = (yield n)
        if newvalue is not None:
            newvalue = n
        else:
            n -= 1
if __name__ == "__main__":
    c = countdown(5)
    for n in c:
        print(n)
        if n == 5:
            c.send(3)
# didnt as it should
# expected output:
# counting down from 5
# 5
# 2
# 1
# 0
# but got:
# counting down from 5
# 5
# 4
# 3
# 2
# 1
# 0