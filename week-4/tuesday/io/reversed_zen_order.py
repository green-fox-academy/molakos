zen = open("reversed_zen_order.txt", "r")
lines = zen.readlines()

for line in lines[::-1]:
    reversed_order = ''
    line = line.rstrip()
    reversed_order = line
    print(reversed_order)

zen.close()
