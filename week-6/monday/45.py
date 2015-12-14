class Pirate():
    def __init__(self, drunkness = 0):
        self.drunkness = drunkness

    def drink_rum(self):
        self.drunkness += 1

    def hows_goin_mate(self):
        if self.drunkness >= 5:
            return 'Arrr!'
        else:
            return 'Nothin\''

pearl = Pirate()

pearl.drink_rum()
print(pearl.hows_goin_mate())
