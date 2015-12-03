filename = 'alma.txt'

def add_A_to_lines(dafile):
    input_file = open(dafile)
    input_content = input_file.read()
    input_file.close()
    output = ''
    for line in input_content.split('\n'):
        output += 'A ' + line + '\n'
    return output


print(add_A_to_lines(filename))

def add_A_to_lines2(dafile):
    input_file = open(dafile)
    lines = input_file.readlines()
    input_file.close()
    for line in lines:
        print('A ' + line.rstrip())

add_A_to_lines2(filename)
