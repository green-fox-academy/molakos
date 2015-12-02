filename = open("alma.txt", "r")



def wc(opened_file):
    filename = open("alma.txt", "r")
    lines = filename.readlines()
    red_lines = 0
    red_char = 0
    for line in lines:
        red_lines += 1
        for char in line:
            red_char += 1
    filename.close()
    return red_lines, red_char

print(wc(filename))

def wc2(opened_file2):
    filename = open("alma.txt", "r")
    lines = filename.readlines()
    red_lines2 = 0
    red_char2 = 0
    for line in lines:
        red_lines2 += 1
        red_char2 += len(line)
    filename.close()
    return red_lines2, red_char2

print(wc2(filename))

def wc3(opened_file3):
    filename = open("alma.txt", "r")
    lines = filename.read()
    line_count = len(lines.split('\n'))
    filename.close()
    return [line_count, len(lines)]

print(wc3(filename))
