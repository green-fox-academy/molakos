class Character():
    def __init__(self, health = 20, armor = 20):
        self._health = health
        self._armor = armor
        self._isAlive = True

    def sufferDamage(self, damage):
        sufferedDamage = self._health + self._armor - damage

        if sufferedDamage < 1:
            self._isAlive = False

    def heal(self, heal):
        self._health += heal

    def getHealth(self):
        return self._health

    def isAlive(self):
        return self._isAlive

def handleEvents(events):
    #list(map(lambda event: eventHandlers[event['type']](event), events))
    list(map(handleEvent, events))

def handleEvent(event):
    eventHandlers[event['type']](event)

def applyHeal(event):
    event['character'].heal(event['size'])

def applyDamage(event):
    event['character'].sufferDamage(event['size'])

eventHandlers = {
    'damage': applyDamage,
    'heal': applyHeal
}
#my own solution:
#    eventList = list(filter(lambda x: x['type'] == 'damage', events))
#    for n in eventList:
#        n['character'].sufferDamage(n['size'])

#    eventList_heal = list(filter(lambda x: x['type'] == 'heal', events))
#    for n in eventList_heal:
#        n['character'].heal(n['size'])




def adder(array):
    return list(map(lambda x: x+1, array))

def filterArray(array):
    return list(filter(lambda x: x % 3 == 0, array))
