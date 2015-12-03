import csv
todo_file = 'todo.csv'

def list_todo(my_items):
    input_todo = open(my_items)
    opened_todo = csv.reader(input_todo, delimiter = '|')
    for index, line in enumerate(opened_todo):
        print([index+1], line[0], line[1])
    input_todo.close()
    return opened_todo

def add_new():
    with open(csv_input, "a") as csvfile:
        # new = input('Add meg az új elemet: ')
        lines = csv.writer(csvfile, delimiter = "|")
        data = ['statusz2', 'leiras2', 20161201,"2016.jan.23"]
        lines.writerow(data)
# add_new()
def remove_item():
    #open list
    my_todo = open(csv_input, "r")
    lines = list(csv.reader(my_todo, delimiter = "|"))
    list_items() # print actual list
    rm = int(input('Melyiket szeretnéd törölni? Adj meg egy számot: '))
    # fill temp list
    temp_list = list(lines)
    print(temp_list[rm-1])
    yes = input('Biztosan törölni akarod? Y/N: ')
    if yes == 'y':
        temp_list.remove(temp_list[rm-1])
        with open(csv_input, "w") as csvfile:
            lines = csv.writer(csvfile, delimiter = "|")
            for line in temp_list:
                lines.writerow(line)
    elif yes == 'n':
        pass
    else:
        print('')
remove_item()
