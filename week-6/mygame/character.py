from random import randint

class Character():
    def __init__(self, name = None, health = 0, dexterity = 0, luck = 0, potion = None):
        self.name = name
        self.health = health
        self.dexterity = dexterity
        self.luck = luck
        self.potion = potion

    def set_health(self):
        self.health = randint(2, 12)+12

    def set_dexterity(self):
        self.dexterity = randint(1, 6)+6

    def set_luck(self):
        self.luck =  randint(1, 6)+6

    def set_potion(self):
        potions = ['Health potion', 'Dexterity potion', 'Luck potion']
        for potion in enumerate(potions):
            print(potion)
        print('Health potion: Set your health back to the base value.')
        print('Health potion: Set your dexterity back to the base value.')
        print('Health potion: Set your luck back to the base value plus add one more.', '\n')
        pick_the_potion = int(input('Please choose a potion! You can only pick one at the time!'))
        self.potion = potions[pick_the_potion]
