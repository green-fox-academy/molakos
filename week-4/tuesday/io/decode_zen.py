zen = open("encoded_zen_lines.txt", "r")
lines = zen.read()

decoded = ''
for character in lines:
    if character == ' ':
        decoded += ' '
    elif character == '\n':
        decoded += '\n'
    else:
        decoded += chr(ord(character)-1)


print(decoded, end='')

zen.close()
