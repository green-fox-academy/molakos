from random import randint

class Character():
    def __init__(self, name = None, health = 0, dexterity = 0, luck = 0):
        self.name = name
        self.max_healt = health
        self.health = health
        self.dexterity = dexterity
        self.max_luck = luck
        self.luck = luck
        self.inventory = ['Leather Armor', 'Sword']

    def character_status(self):
        return self.name, self.health, self.dexterity, self.luck, self.inventory

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
        self.max_healt = self.health
        return self.health

    def set_dexterity(self):
        self.dexterity = randint(1, 6)+6
        return self.dexterity

    def set_luck(self):
        self.luck =  randint(1, 6)+6
        self.max_luck = self.luck
        return self.luck

    def set_potion(self, number):
        potions = ['Potion of Health', 'Potion of Dexterity', 'Potion of Luck']
        #number = int(input('\nPlease choose a potion! You can only pick one at the time!'))
        self.inventory.append(potions[number-1])
        return self.inventory

class Enemy(Character):
    super().__init__(health, dexterity)
    

new_player = Character()
