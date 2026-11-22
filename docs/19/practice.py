goods = [
    ["кеды", 10],
    ["ботинки", 20],
    ["сандалии", 15]
]
count = 0

for item in goods:
    if item[1] > 15:
        print(item[0], "— скидка", item[1], "% — Повышенная скидка")
        count = count + 1
    else:
        print(item[0], "— скидка", item[1], "%")

print("Количество товаров с повышенной скидкой:", count)
