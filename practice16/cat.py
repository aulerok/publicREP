from cats import Cats
p1 = Cats("Барон", "мальчик", 2)
p2 = Cats("Сэм", "мальчик", 2)
if p1.name == p2.name and p1.sex == p2.sex and p1.age == p2.age:
    print(f"\n\t{p1.name} и {p2.name} абсолютно одирнаковые животные")
elif p1.sex == p2.sex and p1.age == p2.age:
    print(f"\n\tУ {p1.name} и {p2.name} Совпадают возраст и пол!")