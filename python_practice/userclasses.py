class User:
    def __init__(self, fullname, balance):
        self.fullname = fullname
        self.balance = balance

    def user_balance(self):
        return self.fullname, self.balance
