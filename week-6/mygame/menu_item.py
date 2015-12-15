class MenuItem:
    def __init__(self, num, name, action):
        self.num = num
        self.name = name
        self.action = action

    def __repr__(self):
        return '{} {}'.format(self.num, self.name)
