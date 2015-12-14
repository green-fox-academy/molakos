battlefield = ([[1,1,0,1,0,0,1,1,1,1],
                [0,0,0,1,0,0,0,0,0,0],
                [1,0,0,1,0,1,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,1,0,0,0,1],
                [0,0,0,0,0,1,0,0,0,1],
                [1,1,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,1,1,1,1]])

class Field:
    def __init__(self, column, row, status):
        self.status = status
        self.column = column
        self.row = row

class Ship(Field):
    def __init__(self):

class AircraftCarrier():

class Battleship():

class Submarine():

class Destroyer():

class PatrolBoat():
