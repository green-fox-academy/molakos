class GameCharacter():
    def __init__(self, name, HP, damage):
        self.name = name
        self.HP = HP
        self.damage = damage

    def print_status(self):
        if self.HP <= 0:
            print(self.name + 'Dead')
        else:
            print(self.name, self.HP)

    def drink_potion(self):
        self.HP += 100
        return self.HP

    def strike(self, other):
        other.HP -= self.damage
        print(other.name + str(other.HP))

class Cerlic(GameCharacter):
    def heal(self, ally):
        ally.HP += 100
        print(ally.name + str(ally.HP))

class Mage(GameCharacter):
    def fireball(self, enemy):
        enemy.HP -= 350
        print(enemy.name + '-350 hp')

paladin = GameCharacter('Thor', 1000, 120)
mage = GameCharacter('Loki', 600, 200)
melkor = Cerlic('Melkor', 1000, 80)

paladin.print_status()
mage.print_status()
for i in range(5):
    paladin.strike(mage)
    melkor.heal(mage)
mage.print_status()
mage.drink_potion()
mage.print_status()
