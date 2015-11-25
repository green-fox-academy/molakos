class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(name, amount):
        self.balance += amount
        return self.balance

    def withdraw(name, amount):
        self.balance -= amount
        return self.balance
