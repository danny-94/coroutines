from follow import follow
def grep(pattern,lines):
    for line in lines:
        if pattern in line:
            yield line 

f = open('input_for_tail')
lines = follow(f)
python_lines = grep('python',lines)
for line in python_lines:
    print(line)
