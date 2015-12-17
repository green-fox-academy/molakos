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
        self.dmg_done = 0

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

    def cast_dice(self):
        random_roll = randint(1, 6)
        return random_roll

    def strike_dmg_counter(self):
        strike_dmg = self.dexterity + self.cast_dice() + self.cast_dice()
        return strike_dmg

    def strike(self, opponent):
        player_strike = self.strike_dmg_counter()
        print('\nYour power: ', player_strike)
        opponent_strike = opponent.strike_dmg_counter()
        print('\nEnemy power: ', opponent_strike, '\n')
        if player_strike == opponent_strike:
            print('Parry!')
            strike(opponent)
        elif player_strike > opponent_strike:
            self.dmg_done = 2
            print('You hit the enemy.\n')
        else:
            print('Enemy hit you.\n')
            opponent.dmg_done = 2

    def after_strike(self, opponent):
        if self.dmg_done > opponent.dmg_done:
            opponent.health -= self.dmg_done
            self.dmg_done = 0
        else:
            self.health -= opponent.dmg_done
            opponent.dmg_done = 0

    def try_luck(self, opponent):
        luck_count = self.cast_dice() + self.cast_dice()
        if self.dmg_done > opponent.dmg_done:
            if luck_count < self.luck:
                opponent.health -= self.dmg_done + 2
            else:
                opponent.health -= self.dmg_done - 1
            self.dmg_done = 0
        else:
            if luck_count < self.luck:
                self.health -= opponent.dmg_done - 1
            else:
                self.health -= opponent.dmg_done + 1
            opponent.dmg_done = 0
        self.luck -= 1

class Enemy(Character):
    def __init__(self, name, health, dexterity):
        super().__init__(name, health, dexterity)

    def print_enemy_status(self):
        stats = [('Name: ' + self.name),
                 ('Health: ' + str(self.health) + '/' + str(self.max_healt)),
                 ('Dexterity: ' + str(self.dexterity))]
        for stat in stats:
            print(stat)


enemy1 = Enemy('bela', 8, 6)
new_player = Character()
