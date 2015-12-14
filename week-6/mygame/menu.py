from character import *

items = [{'name':'New game'},
         {'name':'Load game',},
         {'name':'Exit',}]

newgame_items = [{'name':'Re-enter name'},
                 {'name':'Continue',},
                 {'name':'Save',},
                 {'name':'Quit',}]


class MainMenu():
    def __init__(self, items):
        self.items = items

    def show_menu(self):
        print('\n', '*'*20, '\n')
        for index, item in enumerate(self.items, start=1):
            print(index, item['name'], '\n')
        print('*'*20)

    def execute_chosen_menu_option(self):
        self.show_menu()
        choose = int(input('Welcome to my nightmare! Please choose an option: '))
        try:
            if choose < 1 or choose > 3:
                raise IndexError
            elif choose == 1:
                datnewmenu.add_new_character()
                datnewmenu.new_game_menu()
            elif choose == 2:
                pass
            elif choose == 3:
                pass
            else:
                raise IndexError

        except IndexError:
            print('\033c')
            print('Make sure you pressed the right button. Else I\'m going to break your arm. Try again.')
            datmenu.execute_chosen_menu_option()


class NewGame(MainMenu):
    def __init__(self, items):
        self.items = newgame_items

    def new_game_menu(self):
        newmenu = NewGame(MainMenu(newgame_items))
        newmenu.show_menu()
        choose = int(input('Please choose an option: '))
        if choose == 1:
            datnewmenu.add_new_character()
        elif choose == 2:
            pass
        elif choose == 3:
            pass
        elif choose == 4:
            pass

    def add_new_character(self):
        char_name = input('Please give a name for your character: ')
        self.name = char_name
        print('\n' 'Your charcter\'s name is: ', self.name)

print('\033c')
datmenu = MainMenu(items)
datnewmenu = NewGame(newgame_items)
imported_char = Character()
datmenu.execute_chosen_menu_option()
