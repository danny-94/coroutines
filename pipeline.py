from follow import follow
# follow will wait for the user add new lines to the file "input_file"
def grep(pattern,lines):
    for line in lines:
        if pattern in line:
            yield line 

if __name__ == "__main__":
    f = open('input_file')
    lines = follow(f)
    python_lines = grep('python',lines)
    for line in python_lines:
        print(line)
