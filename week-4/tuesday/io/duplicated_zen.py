zen = open("duplicated_chars.txt", "r")

lines = zen.readlines()


for line in lines:
    line = line.rstrip()
    line = line[::2]
    print(line)

zen.close()
