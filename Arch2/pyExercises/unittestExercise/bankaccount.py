class BankAccount:
    def __init__(self, idc):
        self.idc = idc
        self.balance = 0


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True

        return False

    def deposit(self, amount):
        self.balance += amount
        return True