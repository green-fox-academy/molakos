class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount

    def recieve(self, amount):
        self.balance += amount

    def print_balance(self):
        print(self.name, self.balance)

    def transfer(self, other, amount):
        other.recieve(amount)
        self.pay(amount)


joshi = BankAccount('Joshi Barat', 400)
monika = BankAccount('Monika', 500)

joshi.pay(30)
joshi.print_balance()

monika.transfer(joshi, 50)
joshi.print_balance()
monika.print_balance()
