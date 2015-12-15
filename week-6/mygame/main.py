from menu import Menu
from menu_item import MenuItem
from character import *


def start_game():
    new_player.create_new_character()
    print('\n' 'Your name is: ', new_player.name, '\n')
    main(newgame_menu)

def load_game():
    print('kolbaszt toltse')

def exit_game():
    user_input = input('Are you sure to quit? ')
    if user_input.lower() == 'y':
        pass

menu_list = Menu([
    MenuItem(1, 'New game', start_game),
    MenuItem(2, 'Load game', load_game),
    MenuItem(3, 'Exit', exit_game)
                ])

def re_enter_name():
    new_player.rename_character()
    main(newgame_menu)

def continue_game():
    new_player.set_health()
    new_player.set_dexterity()
    new_player.set_luck()
    print('\n' 'Your stat after random roll:')
    print('\n', 'Health: ', new_player.health, '| Dexterity: ', new_player.dexterity, '| Luck: ', new_player.luck)
    main(reroll_menu)

def save_game():
    pass

def quit_game():
    main(menu_list)

newgame_menu = Menu([
    MenuItem(1, 'Re-enter name', re_enter_name),
    MenuItem(2, 'Continue', continue_game),
    MenuItem(3, 'Save', save_game),
    MenuItem(4, 'Quit', quit_game)
                 ])

def reroll_stats():
    continue_game()

def continue_game_after_roll():
    pass

def save_game_after_reroll():
    pass

reroll_menu = Menu([
    MenuItem(1, 'Reroll stats', reroll_stats),
    MenuItem(2, 'Continue', continue_game_after_roll),
    MenuItem(3, 'Save', save_game_after_reroll),
    MenuItem(2, 'Quit', quit_game)
                ])

def main(selected_menu):
    selected_menu.show_menu()
    user_input = int(input('Please choose an option: '))
    chosen = selected_menu.check_if_valid(user_input)
    try:
        if chosen == True:
            selected_menu.execute_menu_item(user_input)
        else:
            raise ValueError

    except ValueError:
        print('\033c')
        print('Make sure you pressed the right button. Else I\'m going to break your arm. Try again.')


main(menu_list)
