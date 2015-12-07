import commands
import sys

def menu ():
    print("\033c")
    print('*********************************************************')
    print(' * * * *                                         * * * * ')
    print('* * *                1 List items                   * * *')
    print(' * *                 2 Add a new item                * * ')
    print('*                    3 Remove an item                   *')
    print(' * *                 4 Complete an item              * * ')
    print('* * *                5 Exit program                 * * *')
    print(' * * * *                                         * * * * ')
    print('*********************************************************')

    choosen = input("Choose an option: ")

    if choosen == '1':
        print()
        print("\033c")
        commands.list_todo()
        input('For main menu hit enter ')
        menu()
    elif choosen == '2':
        commands.add_new()
        commands.list_todo()
        input('For main menu hit enter ')
        menu()
    elif choosen == '3':
        commands.remove_item()
        print()
        commands.list_todo()
        input('For main menu hit enter ')
        menu()
    elif choosen == '4':
        commands.list_todo()
        commands.make_complete()
        commands.list_todo() #???!
        commands.list_todo()
        input('For main menu hit enter ')
        menu()
    elif choosen.upper() == 'Q':
        pass


menu()
