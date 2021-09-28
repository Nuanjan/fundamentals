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

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.05, balance=0)
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)	# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}", end=' ')
        self.account.display_account_info()
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


user1 = User("Noon", "noon@moon.com")
user1.make_deposit(100).make_deposit(100).display_user_balance()
user2 = User("Roy", "roy@boy.com")
user2.make_deposit(100).make_withdrawal(50).make_deposit(500).display_user_balance()