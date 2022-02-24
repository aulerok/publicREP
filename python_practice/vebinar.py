import random
num = random.randint(1, 100)
print("Угадай число которое я загадал?")
while True:
    guess = int(input())
    if guess == num:
        print("поздравляю умник ты отгадал.")
        break
    elif guess < num:
        print("Нет. Мое число больше.")
    elif guess > num:
        print("Нет. Мое число меньше.")
