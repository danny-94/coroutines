import time 
def follow(f):
    f.seek(0,2)
    while True:
        for line in f:
            if not line:
                time.sleep(0.1)    
                continue 
            yield line 
# logfile = open('input_for_tail')
# for line in follow(logfile):
#     print(line)