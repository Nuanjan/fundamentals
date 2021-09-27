class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

    

user1 = User("Noon", "noon@moon.com")
user1.make_deposit(100)
user1.make_deposit(500)
user1.make_withdrawal(50)
user2 = User("Bee", "bee@hive.com")
user2.make_deposit(2000)

user1.display_user_balance()
user2.display_user_balance()

user1.transfer_money(user2, 50)
user1.display_user_balance()
user2.display_user_balance()

