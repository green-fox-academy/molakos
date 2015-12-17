from menu import Menu
from menu_item import MenuItem
from character import *
from colors import red, green, yellow, cyan

def clear_screen():
    print('\033c')

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
    print('\n' 'Your name is: ', new_player.name, '\n')
    main(newgame_menu)

def continue_game():
    new_player.set_health()
    new_player.set_dexterity()
    new_player.set_luck()
    print('\n' 'Your stat after random roll:')
    print('\n', red('Health: '), new_player.health, '| ', cyan('Dexterity: '), new_player.dexterity, '| ', yellow('Luck: '), new_player.luck, '\n')
    main(reroll_menu)

def save_game():
    pass

def quit_game():
    clear_screen()
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
    clear_screen()
    print('\nPlease select a potion. Choose wisely!')
    print('\nPotion of Health: Set your health back to the base value.')
    print('\nPotion of Dexterity: Set your dexterity back to the base value.')
    print('\nPotion of Luck: Set your luck back to the base value plus add one more.', '\n')
    main(potion_menu)

def save_game_after_reroll():
    pass

reroll_menu = Menu([
    MenuItem(1, 'Reroll stats', reroll_stats),
    MenuItem(2, 'Continue', continue_game_after_roll),
    MenuItem(3, 'Save', save_game_after_reroll),
    MenuItem(4, 'Quit', quit_game)
                ])

def pick_potion(number):
    new_player.set_potion(number)
    print('\nYour pick is: ', new_player.inventory[-1], '\n')
    main(after_potpick_menu)

potion_menu = Menu([
    MenuItem(1, 'Potion of Health', pick_potion, 1),
    MenuItem(2, 'Potion of Dexterity', pick_potion, 2),
    MenuItem(3, 'Potion of Luck', pick_potion, 3),
    MenuItem(4, 'Quit', quit_game)
                ])

def begin_new_game():
    print('\033c')
    print('\nHere is your character:', new_player.name)
    print('\n', red('Health: '), new_player.health, '| ', cyan('Dexterity: '), new_player.dexterity, '| ', yellow('Luck: '), new_player.luck)
    print('\nYour inventory contains: ', new_player.inventory, '\n')
    main(begin_new_game_menu)

after_potpick_menu = Menu([
    MenuItem(1, 'Repick potion', continue_game_after_roll),
    MenuItem(2, 'Continue', begin_new_game),
    MenuItem(3, 'Save', None),
    MenuItem(4, 'Quit', quit_game)
                        ])

def begin_the_game():
    print('\nTest your Sword in a test fight!\n')
    new_player.print_character_status()
    print('\nYour enemy\'s stat: \n')
    enemy1.print_enemy_status()
    print('\n')
    main(fight_menu)

begin_new_game_menu = Menu([
    MenuItem(1, 'Begin', begin_the_game),
    MenuItem(2, 'Save', None),
    MenuItem(3, 'Quit', quit_game)
                            ])

def strike_option():
    new_player.strike(enemy1)
    main(after_strike_menu)

fight_menu =Menu([
    MenuItem(1, 'Strike', strike_option),
    MenuItem(2, 'Retreat', None),
    MenuItem(3, 'Quit', quit_game)
                    ])

def after_strike_option():
    new_player.after_strike(enemy1)
    print('\nYour stat: \n')
    new_player.print_character_status()
    print('\nYour enemy\'s stat: \n')
    enemy1.print_enemy_status()
    print('\n')
    main(fight_menu)

def try_your_luck_option():
    new_player.try_luck(enemy1)
    print('\nYour stat: \n')
    new_player.print_character_status()
    print('\nYour enemy\'s stat: \n')
    enemy1.print_enemy_status()
    print('\n')
    main(fight_menu)

after_strike_menu = Menu([
    MenuItem(1, 'Continue', after_strike_option),
    MenuItem(2, 'Try your luck', try_your_luck_option),
    MenuItem(3, 'Retreat', None),
    MenuItem(4, 'Quit', quit_game)
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
        clear_screen()
        print('Make sure you pressed the right button. Else I\'m going to break your arm. Try again.')

clear_screen()
main(menu_list)
