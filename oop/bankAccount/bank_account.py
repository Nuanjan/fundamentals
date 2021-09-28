class BankAccount:
    bank_name = "Nation Bank"
    def __init__(self, int_rate=0.03, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}, Interest Rate: {self.int_rate}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("No interest at this time, Your balance is zero or Negative")
        return self
    @classmethod
    def change_bank_name(cls,name):
        cls.blank_name = name
        print(f"Bank Name: {cls.blank_name}")         

noon = BankAccount()
noon.deposit(50).deposit(100).deposit(50).withdraw(50).yield_interest().display_account_info()
other = BankAccount(0.05, 100)
other.deposit(100).withdraw(200).withdraw(100).withdraw(50).withdraw(20).yield_interest().display_account_info()
other1 = BankAccount(0.02, 300)
other1.deposit(100).deposit(300).withdraw(30).yield_interest().display_account_info()
BankAccount.change_bank_name("Noon Bank")