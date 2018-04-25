# A more disturbing variation of use of broadcast coroutine
from copipe import follow,grep,printer
from cobroadcast import broadcast
if __name__ == "__main__":
    f = open('input_file')
    p = printer()
    follow(f,broadcast([
        grep('python',p),
        grep('perl',p),
        grep('java',p)
        ]
))