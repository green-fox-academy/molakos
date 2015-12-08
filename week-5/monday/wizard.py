from character import Character

class Wizard(Character):
    def __init__(self, name, hp, damage, mana):
        super().__init__(name, hp, damage)
        self.mana = mana

    def strike(self, opponent):
        if self.mana >= 5:
            opponent.hp -= self.damage * 3
            self.mana -= 5
        elif self.mana < 5:
            opponent.hp -= self.damage / 3
