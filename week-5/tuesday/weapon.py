class Bow():
    def __init__(self, weapon):
        self.weapon = weapon
        
    def damage(self):
        return 10

class ArcaneShot():
    def __init__(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() * 2

class TripleShot():
    def _init_(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() * 3

class AimedShot():
    def _init_(self, weapon):
        self.weapon = weapon

    def damage(self):
        return self.weapon.damage() + 30

class Hunter():
    def __init__(self):
        self.hp = 80
        self.weapon = weapon

    def shoot(self, opponent):
        damage = self.weapon.damage()
        opponent.hp -= damage
