# Broadcast to multiple targets
from coroutine import coroutine
@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            item.send(target)

# This takes series of coroutines(targets) and 
# sends received items to all of them
# Example use:
# f = open("input_file")
