class BankAccount:
    def __init__(self, int_rate = 0.1, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, w_amount):
        if self.balance >= w_amount:
            self.balance -= w_amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

x = BankAccount(0.1, 500)

x.deposit(200).withdraw(175).yield_interest().display_account_info()

