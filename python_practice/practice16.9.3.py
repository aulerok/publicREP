from userclasses import User
user_1 = User('Frank Gallagher', 15)
user_2 = User('Fiona Gallagher', 750)
user_3 = User ('Bill Gates', 131_000_000_000)
users = []
users.extend((user_1, user_2, user_3))
for i in users:
    print(i.user_balance())
