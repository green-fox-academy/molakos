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

    def __repr__(self):
        return '{} {}'.format(self.name, self.health, self.dexterity, self.luck)

    def print_character_status(self):
        stats = [('Name: ' + self.name),
                  ('Health: ' + str(self.health) + '/' + str(self.max_healt)),
                  ('Dexterity: ' + str(self.dexterity)),
                  ('Luck: ' + str(self.luck) + '/' + str(self.max_luck)),
                  ('Inventory: ' + str(self.inventory))]
        for stat in stats:
            print(stat)


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

#class Enemy(Character):


enemy1 = Character('bela', 8, 6)
new_player = Character()
