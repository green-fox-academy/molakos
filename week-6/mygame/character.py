from random import randint

class Character():
    def __init__(self, name = None, health = 0, dexterity = 0, luck = 0, potion = None):
        self.name = name
        self.health = health
        self.dexterity = dexterity
        self.luck = luck
        self.potion = potion

    def create_new_character(self):
        user_input = input('Please give a name for your character: ')
        self.name = user_input
        return self.name

    def rename_character(self):
        user_input = input('Please re-enter the name: ')
        self.name = user_input
        return self.name

    def set_health(self):
        self.health = randint(2, 12)+12
        return self.health

    def set_dexterity(self):
        self.dexterity = randint(1, 6)+6
        return self.dexterity

    def set_luck(self):
        self.luck =  randint(1, 6)+6
        return self.luck

    def set_potion(self):
        potions = ['Health potion', 'Dexterity potion', 'Luck potion']
        for potion in enumerate(potions):
            print(potion)
        print('Health potion: Set your health back to the base value.')
        print('Dexterity potion: Set your dexterity back to the base value.')
        print('Luck potion: Set your luck back to the base value plus add one more.', '\n')
        pick_the_potion = int(input('Please choose a potion! You can only pick one at the time!'))
        self.potion = potions[pick_the_potion]
        return self.potion

new_player = Character()
