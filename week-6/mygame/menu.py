from character import Character

class Menu():
    def __init__(self, items):
        self.items = items

    def show_menu(self):
        print('\n','*'*20, '\n')
        for item in self.items:
            print(item, '\n')
        print('*'*20)

    def execute_menu_item(self, number):
        for item in self.items:
            if item.num == number:
                return item.action()

    def check_if_valid(self, number):
        for item in self.items:
            if item.num == number:
                return True
        return False

    def get_user_input(self):
        user_input = input()
        return user_input
