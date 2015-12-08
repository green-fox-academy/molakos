from character import Character

class Cleric(Character):
    def heal(self, ally):
        ally.hp += 10
