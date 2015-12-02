names = ['Zakarias', 'Hans', 'Otto', 'Ole']

def shortest_name(name_list):
    shortest = name_list[0]
    for n in name_list:
        if len(n) < len(name_list):
            shortest = n
    return(shortest)

print(shortest_name(names))
