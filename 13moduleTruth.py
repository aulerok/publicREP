tickets = int(input('Введите количество билетов: '))
total_coast = 0
for i in range( 1, tickets + 1 ):
    age = int(input('Введите возраст для  билета: '))
    if age < 18:
        coast1 = 0
        total_coast += coast1
    elif 18 <= age <= 25:
        coast2 = 990
        total_coast += coast2
    else:
        coast3 = 1390
        total_coast += coast3
if tickets > 3:
    total_coast = int(total_coast * 0.9)
print(f'Сумма к оплате: {total_coast}')