from copipe import follow,printer,grep
# Broadcast to multiple targets
from coroutine import coroutine
@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)

# This takes series of coroutines(targets) and 
# sends received items to all of them
# Example use:
if __name__ == "__main__":
    f = open("input_file")
    follow(f,broadcast([
        grep('python',printer()),
        grep('perl',printer()),
        grep('java',printer())]
    ))
