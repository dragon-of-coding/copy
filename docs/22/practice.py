goods = [
    ["A1", "кеды", 6],
    ["A2", "ботинки", 0],
    ["A3", "сандалии", 12]
]

for item in goods:
    print(item[0], "—", item[1])
    if item[2] == 0:
        print("Нет на складе")
    else:
        print("В наличии:", item[2], "пар")
