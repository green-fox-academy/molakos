class MenuItem:
    def __init__(self, num, name, action, optional = None):
        self.num = num
        self.name = name
        self.action = action
        self.optional = optional

    def __repr__(self):
        return '{} {}'.format(self.num, self.name)
