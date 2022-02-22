from CorporativeClasses import Guest
num_guests = [i for i in range(1, int(input("сколько планируется гостей:")) + 1)]
guests = []
while True:
    for i in num_guests:
        guests.append(Guest(input("Введите полное имя гостя:"),
              input("Введите город гостя:"),
              input("Введите статус Гостя:")))
    break

for i in guests:
    print(f"Гость {i.guest_info()} из {i.guest_city()} статус гостя '{i.guest_status()}'")

