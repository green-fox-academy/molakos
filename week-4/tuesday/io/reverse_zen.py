zen = open("reversed_zen_lines.txt", "r")
outfile = open("rereversed_zen_lines.txt", "w")

lines = zen.readlines()

for line in lines:
    reversed_line = ''
    line = line.rstrip()
    reversed_line = line[::-1]
    outfile.write(reversed_line + '\n')


zen.close()
outfile.close()

print('ready')
