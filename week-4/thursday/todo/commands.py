import sys
import csv
import time
from datetime import datetime
from colors import red, green, yellow
todo_file = 'todo.csv'

def list_todo():
    input_todo = open(todo_file, 'r')
    lines = csv.reader(input_todo, delimiter = '|')
    print(' Priority:  Description:    Status:   Deadline: '  )
    for index, line in enumerate(lines):
        print(index+1, line[0:3])

    print()
    print()
    input_todo.close()

def add_new():
    with open(todo_file, "a") as csvfile:
        todo_csv = csv.writer(csvfile, delimiter = "|", lineterminator="\n")
        status = 'active'
        priority = input('Choose a priority: H - High, M - Medium, L - Low: ').upper()
        if priority == 'H':
            priority_mod = "  High   "
        elif priority == 'M':
            priority_mod = " Medium  "
        elif priority == 'L':
            priority_mod = "  Low    "
        else:
            priority_mod = " Medium  "
        description = input('Give the description: ')
        deadline = int(input('Please give the deadline (in the following format: 20140602): '))
        date = datetime.now().strftime('%d/%m/%Y %H:%M')
        data = [priority_mod, description, status, deadline, date]
        todo_csv.writerow(data)

def remove_item():
    #open list
    my_todo = open(todo_file, "r")
    lines = list(csv.reader(my_todo, delimiter = "|"))
    list_todo() # print actual list
    rm = int(input('Which one would you like to delete? Please give a number: '))
    # fill temp list
    temp_list = list(lines)
    print(temp_list[rm-1])
    yes = input('Are you sure to remove selected item Y/N: ')
    if yes == 'y':
        temp_list.remove(temp_list[rm-1])
        with open(todo_file, "wb") as csvfile:
            lines = csv.writer(csvfile, delimiter = "|")
            for line in temp_list:
                lines.writerow(line)
    elif yes == 'n':
        print('Remove aborted')
    else:
        print('')

    def make_complete():
        my_todo = open(csv_input, "r")
        lines = list(csv.reader(my_todo, delimiter = "|"))
        rm = int(input('Which one is complete? '))
        temp_list = list(lines)

        print() #empty line
        print('Are you sure? Y/N:')
        print(temp_list[rm-1])
        yes = input('')

        if yes == 'y':
            # add item to the comlete list csv
            with open(csv_complete, "a") as csvfile:
                lines = csv.writer(csvfile, delimiter = "|")
                lines.writerow(temp_list[rm-1])

            temp_list.remove(temp_list[rm-1])
            with open(csv_input, "w") as csvfile:
                lines = csv.writer(csvfile, delimiter = "|")

                for line in temp_list:
                    lines.writerow(line)

                print("\033c") #screen clr
                print('Todo is completed')

        elif yes == 'n':
            print('Abort')
        else:
            print('')
