goods = [
    ["A1", "кеды", 2500, 6],
    ["A2", "ботинки", 4800, 0],
    ["A3", "сандалии", 1900, 12]
]
print("Каталог обуви")

for item in goods:
    print("Артикул:", item[0])
    print("Название:", item[1])
    print("Цена:", format(item[2], ".2f"), "руб.")
    print("Остаток:", item[3])
    print("---")

print("Количество наименований:", len(goods))
